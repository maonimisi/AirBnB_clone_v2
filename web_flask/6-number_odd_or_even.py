#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''
    Function display “Hello HBNB!”
    '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''
    Function display “HBNB!”
    '''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    '''
    display “C ” followed by the value of the text variable
    '''
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonisfun(text='is cool'):
    '''
    display “Python ”, followed by the value of the text
    default value of text is “is cool”
    '''
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def isitanumber(n):
    '''
    display “n is a number” only if n is an integer
    '''
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''
    display a HTML page only if n is an integer
    H1 tag: “Number: n” inside the tag BODY
    '''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    '''
    display a HTML page only if n is an integer
    H1 tag: “Number: n is even|odd” inside the tag BODY
    '''
    if n % 2 == 0:
        status = 'even'
    else:
        status = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, status=status)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
