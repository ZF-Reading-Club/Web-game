import json
import logging

from flask import Response, jsonify, Request
from flask_jwt_extended import create_access_token, set_access_cookies, unset_jwt_cookies

from flask_app.misc.constants import ERROR, SUCCESS

logger = logging.getLogger(__name__)


def sing_in(request: Request) -> tuple[Response, int]:
    """Attempt to log into game with credentials received with the request from user.

    Returns:
        tuple: A Response object with login status and message, response code.
    """
    credentials = request.get_json()
    username = credentials.get("username")
    password = credentials.get("password")
    logger.info("Received data: {credentials}...")
    if not username:
        return jsonify(login=False, message=f"{ERROR}: No username provided!"), 400
    if not password:
        return jsonify(login=False, message=f"{ERROR}: No password provided!"), 400
    valid: bool = validate_credentials(username, password)
    if valid:
        response: Response = authenticate_user(username)
        return response, 200
    return jsonify(login=False, message=f"{ERROR}: Invalid credentials!"), 401


def validate_credentials(username: str, password: str) -> bool:
    """Check if provided login credentials match an existing user.

    Args:
        username (str): Username.
        password (str): Password.

    Returns:
        bool: True if username and password match and existing user, False otherwise.
    # TODO: Implement a proper database connection and query here.
    """
    with open("flask_app/mock_database.json", "r") as file:
        database = json.load(file)
    users = database["users"]
    for user in users:
        if user["username"] == username:
            logger.info(f"Found user: {username} in database...")
            if user["password"] == password:
                logger.info(f"{SUCCESS}: Valid password, logging in...")
                return True
            else:
                logger.error(f"Invalid password for user: {username}. Login failed!")
    logger.error(f"Invalid credentials for user: {username}. Login failed!")
    return False


def authenticate_user(username: str) -> Response:
    """Authenticate user. Create a access JWT token and set it as a cookie with returned response.

    Generates a JWT token string with given username identity. Sets the token as a cookie in the response.

    Args:
        username (str): Username.

    Returns:
        Response: Response object with access cookie containing the JWT token.
    """
    logger.info(f"Authenticating user: {username}...")
    token: str = create_access_token(identity=username)
    response: Response = jsonify(login=True, message=f"Login successful for user: {username}")
    set_access_cookies(response, token)
    logger.info(f"Generated token for user: {token}")
    logger.info(f"Generated response: {response}")
    return response


def log_out() -> Response:
    """Logout user. Deactivate JWT token cookie.

    Invalidate the JWT token cookie in the response signaling the user browser to delete the cookie.

    Returns:
        Response: Response object with deactivated jwt token cookie.
    """
    response = jsonify(logout=True, message="Logout successful")
    logger.info("Unsetting access cookie...")
    unset_jwt_cookies(response)
    return response
