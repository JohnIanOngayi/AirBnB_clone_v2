#!/usr/bin/python3
"""
Script that populates the States and related Cities tab
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def render_cities_by_state():
    """Renders the states tab"""
    states_dicts = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states_dicts)


@app.teardown_appcontext
def shutdown_session(exception=None):
    """Closes current session or deserialises JSON into objects"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
