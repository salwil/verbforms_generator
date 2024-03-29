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

import logging

from flask import Flask, render_template, request, send_file, current_app, flash
from flask_wtf import FlaskForm
from wtforms import BooleanField, RadioField

from src.verbforms_generation.verbforms_generation.csv_file import CsvFile
from src.verbforms_generation.verbforms_generation.lemmatize import GermanLemmatizer
from src.verbforms_generation.verbforms_generation.sentence_generation import SentenceGenerator
from src.verbforms_generation.verbforms_generation.verbforms import Verbforms

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
logging.basicConfig(level=logging.DEBUG)

app_ctx = app.app_context()
app_ctx.push()


class TimeFormsCheckbox(FlaskForm):
    # todo: if time, make general form, by also including verb in form
    #  (currently separately handled, design could ev. be improved)
    praesens = BooleanField('Präsens', default=True, render_kw={'checked': ''})
    praeteritum = BooleanField('Präteritum')
    imperativ = BooleanField('Imperativ (n.a.)')
    konjunktiv1 = BooleanField('Konjunktiv I')
    konjunktiv2 = BooleanField('Konjunktiv II')
    perfekt = BooleanField('Perfekt')
    plusquamperfekt = BooleanField('Plusquamperfekt')
    futur1 = BooleanField('Futur I')
    futur2 = BooleanField('Futur II')


class SentenceFormRadio(FlaskForm):
    sample_sentence = RadioField('Sample sentence:', coerce=str, choices=[('no', 'No'), ('yes', 'Yes')],
                                 default='no')


@app.route('/verbforms_generator')
def welcome():
    # todo: find out how csv_file_for_verbs can be re-initialized
    current_app.config['verb_file'] = CsvFile()
    # initialize Lemmatizer here, so that we do not have to load it for every verb again
    current_app.config['lemmatizer'] = GermanLemmatizer()
    radio = SentenceFormRadio()
    return render_template('welcome.html', radio=radio)


@app.route('/verbforms_generator', methods=['POST'])
def verbforms_generator():
    checkboxes = TimeFormsCheckbox()
    radio = SentenceFormRadio()
    verb = request.form['next_verb']
    current_app.config['verb'] = Verbforms(verb, current_app.config['lemmatizer'])
    if current_app.config['verb'].verb:
        if radio.sample_sentence.data == 'yes':
            try:
                print('try')
                print(current_app.config['verb'].verb.german_conjugations)
                current_app.config['verb'].verb.sample_sentence_german = current_app.config['sentence_generator'] \
                    .generate(current_app.config['verb'].verb.german_conjugations)
            except KeyError:
                print('except')
                print(current_app.config['verb'].verb.german_conjugations)
                current_app.config['sentence_generator'] = SentenceGenerator()
                current_app.config['verb'].verb.sample_sentence_german = current_app.config['sentence_generator'] \
                    .generate(current_app.config['verb'].verb.german_conjugations)
        else:
            try:
                generated_sentence = current_app.config['verb'].verb.sample_sentence_german = None
            except AttributeError:
                generated_sentence = None
        # if current_app.config['verb'].verb:
        return render_template('verbforms_generator.html',
                               next_verb=current_app.config['verb'].verb.infinitive_german,
                               english_translation=current_app.config['verb'].verb.infinitive_english,
                               conjugation_table=current_app.config['verb'].verb.german_conjugations,
                               language_level=current_app.config['verb'].verb.language_level,
                               is_regular=current_app.config['verb'].verb.is_regular,
                               checkboxes=checkboxes,
                               radio=radio,
                               generated_sentence=current_app.config['verb'].verb.sample_sentence_german)
    else:
        return render_template('verbforms_generator.html',
                               next_verb=None,
                               english_translation=None,
                               conjugation_table=None,
                               checkboxes=checkboxes,
                               radio=radio,
                               )


@app.route('/verbforms_generator/add', methods=['POST'])
def add_verb_to_list():
    current_app.config['verb_file']
    checkboxes = TimeFormsCheckbox()
    radio = SentenceFormRadio()
    # current list of timeforms in verbforms.py: ['Präsens', 'Präteritum', 'Perfekt', 'Plusquamperfekt', 'Futur I', 'Futur II', 'Konjunktiv Präsens', 'Konjunktiv Präteritum']
    list_of_timeforms = [checkboxes.praesens.data,
                         checkboxes.praeteritum.data,
                         # checkboxes.imperativ.data,
                         checkboxes.perfekt.data,
                         checkboxes.plusquamperfekt.data,
                         checkboxes.futur2.data,
                         checkboxes.futur1.data,
                         checkboxes.konjunktiv1.data,
                         checkboxes.konjunktiv2.data
                         ]
    current_app.config['verb_file'].write_record(current_app.config['verb'].verb, list_of_timeforms)
    return render_template('verbforms_generator.html',
                           next_verb=current_app.config['verb'].verb.infinitive_german,
                           english_translation=current_app.config['verb'].verb.infinitive_english,
                           conjugation_table=current_app.config['verb'].verb.german_conjugations,
                           language_level=current_app.config['verb'].verb.language_level,
                           is_regular=current_app.config['verb'].verb.is_regular,
                           checkboxes=checkboxes,
                           radio=radio,
                           generated_sentence=current_app.config['verb'].verb.sample_sentence_german)


@app.route('/verbforms_generator/generate')
def generate_artefacts():
    return render_template('download.html')


@app.route('/verbforms_generator/download')
def download_file_with_verbs():
    try:
        return send_file(current_app.config['verb_file'].file_path)
    except FileNotFoundError:
        # todo: alert if no verbs have been added to the file doesn't work yet
        flash('You have not added any verb to your file so far.')
    checkboxes = TimeFormsCheckbox()
    radio = SentenceFormRadio()
    #return render_template('welcome.html', radio=radio)
    return render_template('verbforms_generator.html',
                           next_verb=current_app.config['verb'].verb.infinitive_german,
                           english_translation=current_app.config['verb'].verb.infinitive_english,
                           conjugation_table=current_app.config['verb'].verb.german_conjugations,
                           language_level=current_app.config['verb'].verb.language_level,
                           is_regular=current_app.config['verb'].verb.is_regular,
                           checkboxes=checkboxes,
                           radio=radio,
                           generated_sentence=current_app.config['verb'].verb.sample_sentence_german)


@app.route('/verbforms_generator/goodbye')
def goodbye():
    return render_template('download.html')
