import logging
import os
from flask import Flask
from werkzeug.exceptions import RequestEntityTooLarge

from .config import Config
from .extensions import limiter, csrf
from .routes import bp as main_bp

def create_app(config_class=Config):
    # Configure logging
    logging.basicConfig(
        level=logging.INFO if os.environ.get("FLASK_ENV") != "development" else logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger(__name__)

    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    limiter.init_app(app)
    csrf.init_app(app)

    # Register blueprints
    app.register_blueprint(main_bp)

    # Error handlers
    @app.errorhandler(RequestEntityTooLarge)
    def handle_file_too_large(e):
        from flask import flash, redirect, request
        max_mb = app.config['MAX_CONTENT_LENGTH'] // (1024 * 1024)
        flash(f'File too large. Maximum size is {max_mb}MB.')
        logger.warning("File upload rejected: size limit exceeded")
        return redirect(request.url)

    @app.errorhandler(429)
    def ratelimit_handler(e):
        from flask import flash, redirect, request
        flash("Rate limit exceeded. Please try again later.")
        logger.warning(f"Rate limit exceeded: {e.description}")
        return redirect(request.url)

    return app
