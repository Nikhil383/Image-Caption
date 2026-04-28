from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_wtf.csrf import CSRFProtect

# Initialize extensions without app
limiter = Limiter(
    key_func=get_remote_address,
    # default_limits provided by app config
)

csrf = CSRFProtect()
