import os
import logging
from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman

# Create Flask application
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS)
CORS(app)

# Configure Talisman Security Headers
csp = {
    'default-src': '\'self\'',
    'object-src': '\'none\''
}

Talisman(
    app,
    content_security_policy=csp,
    force_https=False,  # Set to True in production with SSL
    strict_transport_security=True,
    session_cookie_secure=True,
    frame_options='DENY'
)

# Import routes after application initialization to prevent circular imports
from service import routes, models

# Setup logging
logging.basicConfig(level=logging.INFO)
app.logger.info("Service initialized with Talisman and CORS policies.")