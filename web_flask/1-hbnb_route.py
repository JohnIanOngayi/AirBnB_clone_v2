#!/usr/bin/python3

"""
Script Starts A Flask Application
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def root():
    """
    Returns 'HELLO HBNB' when root is queried
    """
    return "HELLO HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Returns 'HELLO HBNB' when /hbnb is queried
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
