import os
import logging
from . import create_app

# Create the application instance
app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_ENV") == "development"
    
    logger = logging.getLogger(__name__)
    logger.info(f"Starting Flask app on port {port}, debug={debug}")
    
    app.run(debug=debug, host="0.0.0.0", port=port)
