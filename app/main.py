r"""Main module for the Flask app.

To run the app in the test environment, run:
src\backend\run_server.bat

To run pytest and show the coverage HTML report, run:
src\backend\run_pytest.bat
"""

import logging
from datetime import datetime

from flask import Flask, jsonify
from flask_cors import CORS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)


def health_check_response(status: str = "ok") -> dict:
    """Create a response dictionary with status and timestamp.

    Args:
        status (str): The status of the response. Defaults to "ok".

    Returns:
        dict: A response dictionary with status and timestamp.
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    response = {"status": status, "message": f"Server response at {current_time}"}
    logger.info(f"Response: {response}")
    return response


@app.route("/api/test", methods=["GET"])
def health_check() -> dict:
    """Test endpoint that returns status and timestamp.

    Returns:
        dict: A response dictionary from health_check_response().
    """
    logger.info("Handling request to /api/test")
    return jsonify(health_check_response())


def create_app() -> Flask:
    """Factory function to create the Flask app.

    Returns:
        Flask: A new Flask app instance.
    """
    return app


if __name__ == "__main__":
    app.run(debug=True)
