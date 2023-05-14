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


@dataclass
class Verb:
    infinitive_german: str = field(init=True, repr=True)
    infinitive_english: str = field(init=True, repr=True)
    german_conjugations: list = field(init=True)
    # english_conjugations: list = field(init=True)
    language_level: str = field(init=True, repr=True)
    sample_sentence_english: str = field(init=False)
    sample_sentence_german: str = field(init=False)
    is_regular: bool = field(repr=True, default=True)
