import multiprocessing
import time

import requests

from src.backend.main import app


def run_flask_app():
    """Run the Flask app in a separate process."""
    app.run(port=5000)


def server():
    """Start the server as a separate process before tests and terminate after."""
    proc = multiprocessing.Process(target=run_flask_app)
    proc.start()
    # Give the server a moment to start
    time.sleep(1)
    yield
    proc.terminate()
    proc.join()


class TestServer:
    def test_live_server_response(server):
        """Test the actual HTTP response from a running server."""
        response = requests.get("http://localhost:5000/api/test")
        assert response.status_code == 200

        data = response.json()
        assert data["status"] == "ok"
        assert "message" in data
        assert "Server response at" in data["message"]
