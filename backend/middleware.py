# backend/middleware.py
from flask import jsonify
import logging

def setup_middleware(app):
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    
    # Global error handler
    @app.errorhandler(Exception)
    def handle_error(e):
        logging.error(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

    # Logging middleware for requests
    @app.before_request
    def log_request_info():
        logging.info(f"Request: {request.method} {request.url}")
