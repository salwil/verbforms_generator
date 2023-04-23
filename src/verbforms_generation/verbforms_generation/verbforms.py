# -*- coding: utf-8 -*-

# verbforms_ui.py

"""
Computer-assisted language learning: verbforms list generation

Jana Hofmann, Salome Wildermuth
Matrikel-Nr: 17-709-361, 10-289-544
University of Zurich
Institute for Computational Linguistics

- read verbforms from https://www.verbformen.de/ and prepare them for csv file

"""
import re
import urllib
from urllib import request

from src.verbforms_generation.verbforms_generation.verb import Verb

class Verbforms:
    def __init__(self, verb: str):
        self.verb_in_any_form: str = verb
        self.verb_html = self.read_html_for_given_verb()
        self.conjugation_table = self.parse_html_for_verbforms()
        self.verb: Verb = None
        self.language_level = self.parse_html_for_language_level()
        self.build_verb_object()

    def read_html_for_given_verb(self):
        url = 'https://www.verbformen.de/?'
        params = {'w': self.verb_in_any_form}
        # Bsp Format: https://www.verbformen.de/?w=gehen
        with request.urlopen(url + urllib.parse.urlencode(params)) as response:
            html = response.read().decode("utf-8")
            return re.sub('\n', '', html)

    def build_verb_object(self):
        self.verb = Verb(self.parse_html_for_infinitive(), [], self.language_level)
        praesens_conjugation = self.conjugation_table[0].split(', ')
        praesens_conjugation[0] = praesens_conjugation[0].replace('Präsens: ', '')
        past_conjugation = self.conjugation_table[1].split(', ')
        past_conjugation[0] = past_conjugation[0].replace('Präteritum: ', '')
        # todo: second element in tuple shall be past instead of present (not implemented yet)
        for present, past in zip(praesens_conjugation, past_conjugation):
            self.verb.german_conjugations.append((present, past))

    def parse_html_for_infinitive(self):
        infinitive_html = re.findall(r'<title>Konjugation .*</title>', self.verb_html)[0]
        infinitive = re.search(
            '%s(.*)%s' % ('<title>Konjugation "',
                          '" - Alle Formen des Verbs, Beispiele, Regeln | Netzverb Wörterbuch</title>'),
            infinitive_html).group(1)
        return infinitive

    def parse_html_for_verbforms(self):
        #verb = re.findall(r'<tr><td>ich </td><td>geh.*</td>', text)
        verb_forms_raw = re.findall(r'Präsens</b>:.*</li>', self.verb_html)[0]
        verb_forms_raw = verb_forms_raw.replace('</b>:', ': ')
        verb_forms_raw = verb_forms_raw.replace('<li>', ' ')
        verb_forms_raw = verb_forms_raw.replace('</li> ', '')
        verb_forms_raw = verb_forms_raw.replace('</li>\t', '')
        verb_forms_raw = verb_forms_raw.replace('\t', '')
        conjugation_table = verb_forms_raw.split(r'<b>')
        return conjugation_table

    def parse_html_for_language_level(self):
        lang_level_html = re.findall(r'Das Verb gehört zum Wortschatz des Zertifikats Deutsch bzw. zur Stufe [A-Z][0-9]. </span>', self.verb_html)[0]
        lang_level = re.search(
            '%s([A-Z][0-9])%s' % ('Das Verb gehört zum Wortschatz des Zertifikats Deutsch bzw. zur Stufe ',
                          '. </span>'),
            lang_level_html).group(1)
        return lang_level


