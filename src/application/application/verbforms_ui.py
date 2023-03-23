# -*- coding: utf-8 -*-

# welcome.py

"""
Computer-assisted language learning: verbforms list generation
Jana Hofmann, Salome Wildermuth
Matrikel-Nr: 17-709-361, 10-289-544
University of Zurich
Institute for Computational Linguistics

- main module for maintaining interaction with user
- from https://flask.palletsprojects.com/en/1.1.x/quickstart/
- export FLASK_APP=src/verbforms_generation/verbforms_generation/main.py
- python3.8 -m flask run
- start with flask run and open http://127.0.0.1:5000/ in the browser

"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/verbforms_generator/welcome')
def hello_world(verb=None):
    return render_template('verbforms_generator.html', name=verb)

@app.route('/verbforms_generator/')
@app.route('/verbforms_generator/<verb>')
def get_verb_forms(verb=None):
    return render_template('verbforms_generator.html', name=verb)
