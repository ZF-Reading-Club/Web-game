"""This is the routes file for the flask app. It contains all the routes for the app.
"""

from flask import jsonify, request, render_template

from flask_app import app
from flask_app.server.server_logic import health_check_response


from flask_jwt_extended import jwt_required, create_access_token, set_access_cookies


@app.route("/")
def index() -> str:
    """Index endpoint that returns a simple message.

    Returns:
        str: A simple message.
    """
    app.logger.info("Handling request to /")
    return render_template("sign_in.html")


@app.route("/api/test", methods=["GET"])
@jwt_required()
def health_check() -> dict:
    """Test endpoint that returns status and timestamp.

    Returns:
        dict: A response dictionary from health_check_response().
    """
    app.logger.info("Handling request to /api/test")
    return jsonify(health_check_response())


@app.route("/api/login", methods=["POST"])
def sign_in() -> dict:
    """Test endpoint to sign in.

    Returns:
        dict: A response dictionary from health_check_response().
    """
    app.logger.info("Handling request to /api/login")
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username:
        if username == "ondra" and password == "123":
            app.logger.info(f"Valid credentials for user {username}")
            token = create_access_token(identity=username)
            app.logger.info(f"Generated token for user {token}")
            response = jsonify(login=True, message="Login successful")
            app.logger.info(f"Generated response {response}")
            set_access_cookies(response, token)
            return response, 200
        else:
            return jsonify(success=False, message="Invalid credentials"), 401
    else:
        return jsonify(success=False, message="Missing credentials"), 400
