"""This script is used to run the server.

It is a simple script that imports the app from the app module and by doing so, runs it.
This script is used to start the server and should not be used for any other purpose.
"""

from flask_app import app

if __name__ == "__main__":
    app.run(debug=True)
