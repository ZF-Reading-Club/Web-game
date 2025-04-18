"""This is the routes file for the flask app. It contains all the routes for the app."""

from flask import jsonify, request, render_template, redirect, url_for
from flask.wrappers import Response

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
)

from flask_app import app
from flask_app.server.api.sign_in_logic import sing_in, log_out
from flask_app.server.game_logic.health_check import health_check_response


@app.route("/", methods=["GET"])
@jwt_required()
def index() -> str:
    """Home endpoint. Redirects to game page.

    Returns:
        str: HTML game page.
    """
    app.logger.info("Handling request to '/'...")
    return redirect(location=url_for(endpoint="api_game"))


@app.route(rule="/game", methods=["GET"])
@jwt_required()
def api_game() -> str:
    """Actual game page endpoint. User can play game here.

    Valid JWT token is required to access this page. Without it, user is redirected according
    to the '@jwt.unauthorized_loader' definition.

    Returns:
        str: HTML game page.
    """
    app.logger.info("Handling request to '/game'...")
    return render_template("game.html")


@app.route(rule="/login", methods=["GET"])
@jwt_required(optional=True)
def api_login() -> str:
    """Login page endpoint. Provides a login page for users.

    If user is already logged in, they are redirected to the game page. Otherwise, they are redirected to login page.

    Returns:
        str: HTML game or login page.
    """
    app.logger.info("Handling request to '/login'...")
    user = get_jwt_identity()
    if user is not None:
        app.logger.info(f"User: {user} is already logged in. Redirecting to '/game'...")
        return redirect(location=url_for(endpoint="api_game"))
    # login_attempt: tuple[Response, int] = log_in(request=request)
    return render_template(template_name_or_list="login.html")


@app.route("/signin", methods=["POST"])
def api_signin() -> dict:
    """The actual login endpoint. Handles signin requests from login page.

    Returns:
        tuple(Response, int): A Response object with login status and message, response code.
    """
    app.logger.info("Handling request to '/signin'...")
    result: tuple[Response, int] = sing_in(request=request)
    return result


@app.route("/logout", methods=["GET"])
@jwt_required()
def sign_out() -> dict:
    """Logout endpoint.

    Returns:
        dict: A Response object with deactivated jwt token cookie, response code.
    """
    app.logger.info("Handling request to /logout...")
    response = log_out()
    return response, 200


@app.route("/api/test", methods=["GET"])
@jwt_required()
def health_check() -> dict:
    """Test endpoint that returns status and timestamp.

    Returns:
        dict: A response dictionary from health_check_response().
    """
    app.logger.info("Handling request to /api/test")
    return jsonify(health_check_response())
