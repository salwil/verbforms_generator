# -*- coding: utf-8 -*-

# verbforms_ui.py

"""
Computer-assisted language learning: verbforms list generation

Jana Hofmann, Salome Wildermuth
Matrikel-Nr: 17-709-361, 10-289-544
University of Zurich
Institute for Computational Linguistics

- format verbs etc. for index cards and write formatted content to csv file for index cards generation

"""
import csv
from src.verbforms_generation.verbforms_generation.verb import Verb, Praesens, Praeteritum


class IndexCard:
    def __init__(self, verb: Verb):
        self.verb = verb

    def write_card(self, csv_writer):
        csv_writer.writerow([self.verb.infinitive_german] + [self.verb.language_level])
