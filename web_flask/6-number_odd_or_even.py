#!/usr/bin/python3

"""
Script Starts A Flask Application
"""

from flask import Flask, render_template

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


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """
    Returns 'C text' when /c/text is queried
    """
    return f"C {text.replace('_', ' ')}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """
    Returns 'Python text' when /python/text is queried
    """
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """
    Returns 'n is a number' if n is an int
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_route_html(n):
    """
    Renders a html template with number passed
    """
    if isinstance(n, int):
        return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even_route(n):
    """
    Renders a html template with number passed
    """
    if isinstance(n, int):
        if (n % 2):
            st = "odd"
        else:
            st = "even"
        return render_template('6-number_odd_or_even.html', number=n, state=st)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
