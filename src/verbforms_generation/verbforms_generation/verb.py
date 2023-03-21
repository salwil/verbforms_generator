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

from dataclasses import dataclass, field
from enum import Enum

class TimeForm(Enum):
    PRAESENS = 'praesens'
    PRAETERITUM = 'praeteritum'

@dataclass
class Verb:
    infinitive: str = field(init=True, repr=True)
    conjugations: {} = field(init=True)
    language_level: str = field(init=True, repr=True)

@dataclass
class Praesens(Verb):
    timeform: TimeForm = field(default=TimeForm.PRAESENS, init = False)

@dataclass
class Praeteritum(Verb):
    timeform: TimeForm = field(default=TimeForm.PRAETERITUM, init = False)




