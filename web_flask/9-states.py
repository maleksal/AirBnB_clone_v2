#!/usr/bin/python3
"""Flask app module"""
from models import storage
from flask import Flask, render_template
from os import environ

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(session):
    """ Remove current session """
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def hbnb_states_byID_route(id=None):
    """ List all state objects present in database by states_id"""
    from models.state import State

    states = storage.all(State).values()
    if id:
        get_state = None
        for state in states:
            if state.id == id:
                get_state = state
        return render_template("9-states.html", desired_state=get_state)
    return render_template("8-cities_by_states.html", all_states=states)

if __name__ == '__main__':
    environ['FLASK_APP'] = __file__
    app.run(host='0.0.0.0', port=5000)
