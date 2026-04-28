import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Base configuration."""
    # Ensure SECRET_KEY is set in production
    SECRET_KEY = os.environ.get("SECRET_KEY")
    if not SECRET_KEY and os.environ.get("FLASK_ENV") not in ("development", "testing"):
        raise ValueError("No SECRET_KEY set for Flask application in production. Please set the SECRET_KEY environment variable.")
    elif not SECRET_KEY:
        # Development/Testing fallback only
        SECRET_KEY = "dev_secret_key_change_in_production"

    # File upload settings
    MAX_CONTENT_LENGTH_MB = int(os.environ.get("MAX_CONTENT_LENGTH_MB", 10))
    MAX_CONTENT_LENGTH = MAX_CONTENT_LENGTH_MB * 1024 * 1024
    ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp'}

    # Rate Limiter settings
    RATELIMIT_DEFAULT = "100 per day; 20 per hour"
    RATELIMIT_STORAGE_URI = "memory://"  # Default to memory, can be overriden to redis:// in prod
