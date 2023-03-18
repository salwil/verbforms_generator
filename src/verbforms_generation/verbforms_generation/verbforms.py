# -*- coding: utf-8 -*-

# verbforms.py

"""
Computer-assisted language learning: verbforms list generation

Jana Hofmann, Salome Wildermuth
Matrikel-Nr: 17-709-361, 10-289-544
University of Zurich
Institute for Computational Linguistics

- read verbforms from https://www.verbformen.de/ and prepare them for csv file

"""
from urllib import request

class Verbforms:
    def __init__(self, verb: str):
        self.verb_in_any_form: str = verb
        self.verb_data_raw = self.read_html_for_given_verb()

    def read_html_for_given_verb(self):
        with request.urlopen('https://www.verbformen.de/?w=gehen') as response:
            return response.read()

    def extract_verbforms_from_html(self):
        pass
        #todo: extract required data and construct verb object (investigate in html.parser libary)
