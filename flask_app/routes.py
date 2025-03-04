"""This is the routes file for the flask app. It contains all the routes for the app.
"""

from flask import jsonify, request, render_template, redirect, url_for

from flask_app import app
from flask_app.server.server_logic import health_check_response


from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    set_access_cookies,
    get_jwt_identity,
    unset_jwt_cookies,
)


@app.route("/", endpoint="home", methods=["GET"])
@jwt_required()
def index() -> str:
    """Index endpoint that returns a signup page or game page for logged in users.

    Returns:
        str: HTML game or login page.
    """
    app.logger.info("Handling request to /")
    return redirect(url_for("game"))


@app.route(rule="/login", endpoint="login", methods=["GET"])
@jwt_required(optional=True)
def login_page() -> str:
    """Login page endpoint. User can sign in here.

    Returns:
        str: HTML login page.
    """
    app.logger.info("Handling request to /login")
    user = get_jwt_identity()
    if user is not None:
        app.logger.info(f"User: {user} is already logged in. Redirecting to /game")
        return redirect(url_for("game"))
    app.logger.info("No user logged in. Redirecting to sign_in.html")
    return render_template("sign_in.html")


@app.route(rule="/game", endpoint="game", methods=["GET"])
@jwt_required()
def game_page() -> str:
    """Actual game page endpoint. User can play game here.Valid credentials

    Returns:
        str: HTML game page.
    """
    app.logger.info("Handling request to /game")
    return render_template("game.html")


@app.route("/api/test", methods=["GET"])
@jwt_required()
def health_check() -> dict:
    """Test endpoint that returns status and timestamp.

    Returns:
        dict: A response dictionary from health_check_response().
    """
    app.logger.info("Handling request to /api/test")
    return jsonify(health_check_response())


@app.route("/sign_in", methods=["POST"])
def sign_in() -> dict:
    """Test endpoint to sign in.

    Returns:
        dict: A response dictionary from health_check_response().
    """
    app.logger.info("Handling request to /sign_in")
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


@app.route("/logout", methods=["GET"])
@jwt_required()
def sign_out() -> dict:
    """Test endpoint to sign out.

    Returns:
        dict: A response dictionary from health_check_response().
    """
    app.logger.info("Handling request to /logout")
    response = jsonify(logout=True, message="Logout successful")
    app.logger.info(f"Generated response {response}")
    app.logger.info("Unsetting access cookie.")
    unset_jwt_cookies(response)
    return response, 200
