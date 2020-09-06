#!/usr/bin/python3
"""Flask app module"""
from models import storage
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from os import environ

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(session):
    """ Remove current session """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters_route():
    """display state & amenities"""

    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == '__main__':
    environ['FLASK_APP'] = __file__
    app.run(host='0.0.0.0', port=5000)
