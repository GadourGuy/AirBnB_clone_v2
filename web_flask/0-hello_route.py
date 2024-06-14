#!/usr/bin/python3
"""
<<<<<<< HEAD
start Flask application
=======
starts a Flask web application
>>>>>>> 5b8f914524d8d2d49ace9049234b1747fdf9b51e
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
