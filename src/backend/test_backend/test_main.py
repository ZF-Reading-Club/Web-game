import pytest

from src.backend.main import create_app, health_check_response

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app()
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    """Create a test client for the app."""
    return app.test_client()

def test_create_response():
    """Test the create_response function."""
    response = health_check_response()
    assert isinstance(response, dict)
    assert response["status"] == "ok"
    assert "message" in response
    assert "Server response at" in response["message"]

def test_test_endpoint(client):
    """Test the test endpoint."""
    response = client.get('/api/test')
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"
    assert "message" in data
    assert "Server response at" in data["message"]