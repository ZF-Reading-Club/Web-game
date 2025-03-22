"""This file sets up the Flask app.

Code here gets executed when the app object form here gets imported anywhere.
"""

from flask import Flask
from flask_cors import CORS

from flask_jwt_extended import JWTManager


# Create a new Flask app
# App needs to be created before importing routes to avoid circular imports and to ensure that the app object is
# available to the routes.
app = Flask(
    __name__,
    template_folder="frontend/templates",
)
CORS(app)
# Routes need to be imported after the app is created.
from flask_app.server.api import routes

# JWT settings
app.config["JWT_SECRET_KEY"] = "super"
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_COOKIE_SECURE"] = False
app.config["JWT_ACCESS_TOKEN_PATH"] = "/"
app.config["JWT_COOKIE_SAMESITE"] = "Strict"
app.config["JWT_COOKIE_CSRF_PROTECT"] = False

jwt = JWTManager(app)
from flask_app.server.api import jwt_callbacks
