# -*- coding: utf-8 -*-

# verb.py

"""
Computer-assisted language learning: verbforms list generation

Jana Hofmann, Salome Wildermuth
Matrikel-Nr: 17-709-361, 10-289-544
University of Zurich
Institute for Computational Linguistics

- read verbforms from https://www.verbformen.de/ and prepare them for csv file

"""

from dataclasses import dataclass

@dataclass
class Verb:
    infinitive: str (init=True, repr=True)
    present: {'ich': None, 'du': None, 'er/sie/es': None, 'wir': None, 'ihr': None, 'sie': None}

