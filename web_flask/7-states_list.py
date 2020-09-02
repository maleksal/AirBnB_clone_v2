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


@app.route('/states_list', strict_slashes=False)
def hbnb_states_list_route():
    """ List all state objects present in database """
    from models.state import State
    import operator
    states = sorted(
        storage.all(State).values(),
        key=operator.attrgetter("name"))
    return render_template("7-states_list.html", all_states=states)


if __name__ == '__main__':
    environ['FLASK_APP'] = __file__
    app.run(host='0.0.0.0', port=5000)
