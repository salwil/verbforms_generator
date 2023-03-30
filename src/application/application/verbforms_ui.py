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
- for linux: export FLASK_APP=src/application/application/verbforms_ui.py
- for windows: set FLASK_APP=src/application/application/verbforms_ui.py
- python3.8 -m flask run or python -m flask run
- start with flask run and open http://127.0.0.1:5000/ in the browser
- to end control c

"""

from flask import Flask, render_template, request, send_file

from src.verbforms_generation.verbforms_generation.csv_file import CsvFile
from src.verbforms_generation.verbforms_generation.verbforms import Verbforms

app = Flask(__name__)

csv_file_for_verbs = CsvFile()

@app.route('/verbforms_generator')
def welcome():
    return render_template('welcome.html')

@app.route('/verbforms_generator', methods=['POST'])
def verbforms_generator():
    verb=request.form['verb']
    verbforms = Verbforms(verb)
    csv_file_for_verbs.write_record([verbforms.praesens.conjugations['ich'], verbforms.praesens.conjugations['du'], verbforms.praesens.conjugations['er']])
    return render_template('verbforms_generator.html', verb=verbforms.praesens.infinitive)

@app.route('/verbforms_generator/download')
def download_file_with_verbs():
    csv_file_for_verbs.close_file()
    return send_file(csv_file_for_verbs.file_path)