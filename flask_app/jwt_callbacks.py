import logging

from flask import redirect, url_for, request
from werkzeug import Response
from flask_app import jwt

logger = logging.getLogger(__name__)


@jwt.unauthorized_loader
def redirect_to_signin(error: str) -> Response:
    logger.info(f"Invalid authentication: {error}, when accesing: {request.url}. Redirecting to /login")
    return redirect(url_for("login"))
