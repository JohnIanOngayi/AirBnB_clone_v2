#!/usr/bin/python3
"""
Script that populates the States tab
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def render_state():
    """Renders the states tab"""
    states_dicts = storage.all(State).values()
    return render_template('7-states_list.html', states=states_dicts)


@app.route("/states/<id>", strict_slashes=False)
def render_cities_by_state_id(id=None):
    """if id is a valid id render cities to the state"""
    states_dicts = storage.all(State).values()
    for state in states_dicts:
        if id == state.id:
            return render_template('9-states.html', state=state)
    return (
        """<!DOCTYPE html>
        <HTML lang="en">
            <HEAD>
                <TITLE>HBNB</TITLE>
            </HEAD>
            <BODY>

                <H1>Not found!</H1>

            </BODY>
        </HTML>
        """
    )


@app.teardown_appcontext
def shutdown_session(exception=None):
    """Closes current session or deserialises JSON into objects"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
