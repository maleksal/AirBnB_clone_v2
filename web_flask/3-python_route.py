#!/usr/bin/python3
""" Flask Module """


from flask import Flask
from os import environ

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Display Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """Display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hbnb_c_route(text):
    """Display C followed by text"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/(<text>)', strict_slashes=False)
def hbnb_python_route(text="is cool"):
    """Display C followed by text"""
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    environ['FLASK_APP'] = __file__
    app.run(host='0.0.0.0', port=5000)
