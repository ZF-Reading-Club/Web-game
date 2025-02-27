"""This is the routes file for the flask app. It contains all the routes for the app.
"""

from flask import jsonify

from flask_app import app
from flask_app.server.server_logic import health_check_response


@app.route("/api/test", methods=["GET"])
def health_check() -> dict:
    """Test endpoint that returns status and timestamp.

    Returns:
        dict: A response dictionary from health_check_response().
    """
    app.logger.info("Handling request to /api/test")
    return jsonify(health_check_response())
