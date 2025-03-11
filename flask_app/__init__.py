"""This file sets up the Flask app.

Code here gets executed when the app object form here gets imported anywhere.
"""
from datetime import timedelta
from flask import Flask
from flask_cors import CORS

from flask_jwt_extended import JWTManager


# Create a new Flask app
# App needs to be created here before importing routes to avoid circular imports and to ensure that
# the app object is available to the routes.

app = Flask(
    __name__,
)
CORS(app)

from flask_app import routes

# JWT settings
app.config["JWT_SECRET_KEY"] = "super"  # This is the secret key used to encode and decode the JWT tokens
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]  # Token expected in cookies from client. Other methods are headers, query_string, json (client code needed)
# Ex.GET /api/protected HTTP/1.1
# Host: example.com
# Cookie: access_token_cookie=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMjMsImlhdCI6MTY0ODMxNzE3NSwiZXhwIjoxNjQ4MzIxNzc1fQ.dQ5Q_0wU9xIBd6sE72RzRqjXZhUQMC7H6ClwQv2JK8
app.config["JWT_COOKIE_SECURE"] = False  # Allows cookies to be sent over HTTP. True for production - HTTPS.
app.config["JWT_ACCESS_TOKEN_PATH"] = "/"  # Path for which the access token cookie is valid. / means root path - all routes.
app.config["JWT_COOKIE_SAMESITE"] = "Strict"  # This enforces the cookie to be sent only from same domain. Prevents CSRF attacks.
app.config["JWT_COOKIE_CSRF_PROTECT"] = False  # Additional protection against CSRF attacks.
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(seconds=600)

# HTTP/1.1 200 OK
# Content-Type: application/json
# Set-Cookie: access_token_cookie=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...; Path=/; HttpOnly; Secure; SameSite=Strict


jwt = JWTManager(app)

from flask_app import jwt_callbacks
