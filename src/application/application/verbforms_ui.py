# -*- coding: utf-8 -*-

# verbforms_ui.py

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

#csv_file_for_verbs = CsvFile()

class CurrentDialogue():
    def __init__(self):
        self.verb = None
        self.csv_file_for_verbs = CsvFile()

current_dialogue = CurrentDialogue()

@app.route('/verbforms_generator')
def welcome():
    #todo: find out how csv_file_for_verbs can be re-initialized
    current_dialogue.csv_file_for_verbs.open_file()
    return render_template('welcome.html')

@app.route('/verbforms_generator', methods=['POST'])
def verbforms_generator():
    verb=request.form['next_verb']
    current_dialogue.verb = Verbforms(verb)
    print(current_dialogue.verb.verb.german_conjugations)
    #csv_file_for_verbs.write_record(verbforms.verb)
    return render_template('verbforms_generator.html',
                           next_verb=current_dialogue.verb.verb.infinitive_german,
                           english_translation=current_dialogue.verb.verb.infinitive_english,
                           conjugation_table=current_dialogue.verb.verb.german_conjugations)

@app.route('/verbforms_generator/add', methods=['POST'])
def add_verb_to_list():
    print(current_dialogue.verb.verb.german_conjugations)
    current_dialogue.csv_file_for_verbs.write_record(current_dialogue.verb.verb)
    return render_template('verbforms_generator.html',
                           next_verb=current_dialogue.verb.verb.infinitive_german,
                           english_translation=current_dialogue.verb.verb.infinitive_english,
                           conjugation_table=current_dialogue.verb.verb.german_conjugations)

@app.route('/verbforms_generator/download')
def download_file_with_verbs():
    if current_dialogue.csv_file_for_verbs.is_open:
        current_dialogue.csv_file_for_verbs.close_file()
        return render_template('download.html')
    else:
        return send_file(current_dialogue.csv_file_for_verbs.file_path)


@app.route('/verbforms_generator/goodbye')
def goodbye():
    # this is to reduce erroronous behavior of the tool.
    return render_template('download.html')