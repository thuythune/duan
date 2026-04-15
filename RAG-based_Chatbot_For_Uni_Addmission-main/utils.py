import logging
from config import LOG_LEVEL, LOG_FORMAT

def setup_logging():
    """Configures the application-wide logging."""
    logging.basicConfig(level=getattr(logging, LOG_LEVEL.upper(), logging.INFO), format=LOG_FORMAT)