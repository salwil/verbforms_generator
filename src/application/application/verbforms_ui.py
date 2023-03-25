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

from flask import Flask, render_template, request
from src.verbforms_generation.verbforms_generation.verbforms import Verbforms

app = Flask(__name__)

@app.route('/verbforms_generator')
def welcome():
    return render_template('welcome.html')

@app.route('/verbforms_generator', methods=['POST'])
def verbforms_generator():
    verb=request.form['verb']
    verbforms = Verbforms(verb)
    return render_template('verbforms_generator.html', verb=verbforms.praesens.infinitive)
