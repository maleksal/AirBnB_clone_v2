#!/usr/bin/python3
""" Flask Module """


from flask import Flask, render_template
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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hbnb_python_route(text="is cool"):
    """Display C followed by text"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:num>', strict_slashes=False)
def hbnb_number_route(num):
    """Display C followed by text"""
    return '{} is a number'.format(num)


@app.route('/number_template/<int:n>', strict_slashes=False)
def hbnb_number_template_route(n):
    """ """
    return render_template("5-number.html", number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def hbnb_number_oddEven_route(n):
    """ Check if number is odd or even """
    holder = "even" if n % 2 else "odd"
    return render_template(
        "6-number_odd_or_even.html",
        number=n,
        answer=holder)

if __name__ == '__main__':
    environ['FLASK_APP'] = __file__
    app.run(host='0.0.0.0', port=5000)
