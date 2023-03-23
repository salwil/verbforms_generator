# -*- coding: utf-8 -*-

# main.py

"""
Computer-assisted language learning: verbforms list generation

Jana Hofmann, Salome Wildermuth
Matrikel-Nr: 17-709-361, 10-289-544
University of Zurich
Institute for Computational Linguistics

- main module for maintaining interaction with user
- from https://flask.palletsprojects.com/en/1.1.x/quickstart/
- start with flask run and open http://127.0.0.1:5000/ in the browser

"""



from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
