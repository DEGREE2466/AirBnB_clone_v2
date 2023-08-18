#!/usr/bin/python3
""" A script that starts a flask web app """
from flask import Flask
app = Flask(__name__)


@app.route('/airbnb-onepage', strict_slashes=False)
def hello_hbnb():
    """ Prints a Message when / is called """
    return 'Hello, airbnb-onepage!'

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
