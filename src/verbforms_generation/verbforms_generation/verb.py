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
    IMPERATIV = 'imperativ'
    KONJUNKTIV1 = "konjunktiv1",
    KONJUNKTIV2 = "konjunktiv2",
    PERFEKT = "perfekt",
    PLUSQUAMPERFEKT = "plusquamperfekt",
    FUTUR1 = "futur1",
    FUTUR2 = "futur2"

@dataclass
class Verb:
    infinitive_german: str = field(init=True, repr=True)
    infinitive_english: str = field(init=True, repr=True)
    german_conjugations: list = field(init=True)
    #english_conjugations: list = field(init=True)
    language_level: str = field(init=True, repr=True)




