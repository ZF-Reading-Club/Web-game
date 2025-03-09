import json
import logging

from flask import Response, jsonify
from flask_jwt_extended import create_access_token, set_access_cookies

logger = logging.getLogger(__name__)


def mock_user_login(username: str, password: str) -> bool:
    """Mock user login function.

    Args:
        username (str): Username.
        password (str): Password.

    Returns:
        bool: True if username and password are valid, False otherwise.
    """
    with open("flask_app/mock_database.json", "r") as file:
        database = json.load(file)
    users = database["users"]
    for user in users:
        if user["username"] == username:
            logger.info(f"Found user: {username} in database...")
            if user["password"] == password:
                logger.info("Valid password, logging in...")
                return True
            else:
                logger.info("Invalid password, login failed.")
    logger.info(f"Invalid credentials for user: {username}. Login failed.")
    return False


def authenticate_user(username: str) -> Response:
    """Authenticate user and return response.

    Args:
        username (str): Username.

    Returns:
        Response: Response object.
    """
    logger.info(f"Authenticating user: {username}")
    token = create_access_token(identity=username)
    response = jsonify(login=True, message=f"Login successful for user: {username}")
    set_access_cookies(response, token)
    logger.info(f"Generated token for user: {token}")
    logger.info(f"Generated response: {response}")
    return response
