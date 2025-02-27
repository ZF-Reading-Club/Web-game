"""This file sets up the Flask app.

Code here gets executed when the app object form here gets imported anywhere.
"""

from flask import Flask
from flask_cors import CORS

# Create a new Flask app
# App needs to be created here before importing routes to avoid circular imports and to ensure that
# the app object is available to the routes.
app = Flask(__name__)
CORS(app)

from flask_app import routes
