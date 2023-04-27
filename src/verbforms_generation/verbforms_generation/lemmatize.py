# -*- coding: utf-8 -*-

# verb.py

"""
Computer-assisted language learning: verbforms list generation

Jana Hofmann, Salome Wildermuth
Matrikel-Nr: 17-709-361, 10-289-544
University of Zurich
Institute for Computational Linguistics

- use lemmatization, if verb is not found

"""

import spacy
import sys
import traceback

class Lemmatizer:
    def __init__(self):
        pass

    def lemmatize(self, sentence):
        lemmatized_verb = self.nlp(sentence)
        return ' '.join([word.lemma_ for word in lemmatized_verb])

class GermanLemmatizer(Lemmatizer):
    def __init__(self):
        try:
            self.nlp = spacy.load('de_core_news_sm')
        except(IOError):
            traceback.print_exc()
            sys.exit("Have you downloaded de_core_news_sm to your environment?")

class EnglishLemmatizer(Lemmatizer):

    def __init__(self, nlp):
        try:
            self.nlp = nlp
        except(IOError):
            traceback.print_exc('en_core_web_sm')
            sys.exit("Have you downloaded en_core_web_sm to your environment?")


