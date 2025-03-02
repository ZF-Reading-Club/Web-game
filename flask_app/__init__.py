"""This file sets up the Flask app.

Code here gets executed when the app object form here gets imported anywhere.
"""

import os

from flask import Flask
from flask_cors import CORS

from flask_jwt_extended import JWTManager

# Create a new Flask app
# App needs to be created here before importing routes to avoid circular imports and to ensure that
# the app object is available to the routes.

# Determine the absolute path of the current file (app/__init__.py)
app_dir = os.path.dirname(os.path.abspath(__file__))
print("App directory path:", app_dir)
# Build the absolute path to the templates folder (assuming it's at project_root/frontend/templates)
template_path = os.path.join(app_dir, "..", "frontend", "templates")
print("Computed template folder path:", template_path)

# Print the computed path for debugging
print("Computed template folder path:", os.path.abspath(template_path))


app = Flask(
    __name__,
)
CORS(app)

# JWT settings
app.config["JWT_SECRET_KEY"] = "super"
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_COOKIE_SECURE"] = False
app.config["JWT_ACCESS_TOKEN_PATH"] = "/"
app.config["JWT_COOKIE_SAMESITE"] = "Strict"
app.config["JWT_COOKIE_CSRF_PROTECT"] = False

jwt = JWTManager(app)

from flask_app import routes
