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
        self.list_of_timeforms = ['Präsens', 'Präteritum', 'Perfekt', 'Plusquamperfekt', 'Futur I', 'Futur II']
        self.verb_in_any_form: str = verb
        self.verb_html = self.read_html_for_given_verb()
        #self.conjugation_table = self.parse_html_for_verbforms()
        self.conjugation_dict = self.parse_html_for_verbforms()
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
        german_infinitive = self.parse_html_for_german_infinitive()
        english_infinitive = self.parse_html_for_english_infinitive()
        lang_level = self.parse_html_for_language_level()
        if german_infinitive and lang_level:
            self.verb = Verb(german_infinitive, english_infinitive, [], lang_level)
            #for timeform in list_of_timeforms:
            #    self.extract_timeform(timeform, list_of_timeforms.index(timeform))
            # todo: second element in tuple shall be past instead of present (not implemented yet)
                #time = (self.conjugation_dict[timeform][i] for timeform in list_of_timeforms)
            self.verb.german_conjugations = list(zip(self.conjugation_dict['Präsens'], self.conjugation_dict['Präteritum'], self.conjugation_dict['Perfekt'], self.conjugation_dict['Plusquamperfekt'], self.conjugation_dict['Futur II'], self.conjugation_dict['Futur I']))
            #for present, past in zip(praesens_conjugation, past_conjugation):
            #    self.verb.german_conjugations.append((present, past))

    def extract_timeform(self, conjugation_table, timeform: str, index: int):
        conjugation = conjugation_table[index].split(', ')
        conjugation[0] = conjugation[0].replace(timeform + ': ', '')
        return conjugation

    def parse_html_for_german_infinitive(self):
        try:
            infinitive_html = re.findall(r'<title>Konjugation .*</title>', self.verb_html)[0]
            infinitive = re.search(
                '%s(.*)%s' % ('<title>Konjugation "',
                              '" - Alle Formen des Verbs, Beispiele, Regeln | Netzverb Wörterbuch</title>'),
                infinitive_html).group(1)
            return infinitive
        except IndexError:
            return None

    def parse_html_for_verbforms(self):
        try:
            verb_forms_raw = re.findall(r'Präsens</b>:.*</li></ul><h3>Konjunktiv Aktiv', self.verb_html)[0]
            verb_forms_raw = verb_forms_raw.replace('</b>:', ': ')
            verb_forms_raw = verb_forms_raw.replace('<li>', ' ')
            verb_forms_raw = verb_forms_raw.replace('</li> ', '')
            verb_forms_raw = verb_forms_raw.replace('</li></ul><h3>Konjunktiv Aktiv', '')
            verb_forms_raw = verb_forms_raw.replace('</li>\t', '')
            verb_forms_raw = verb_forms_raw.replace('\t', '')
            conjugation_table = verb_forms_raw.split(r'<b>')
            conjugation_dict = {}
            for timeform in self.list_of_timeforms:
                conjugation_dict[timeform] = self.extract_timeform(conjugation_table, timeform, self.list_of_timeforms.index(timeform))
            return conjugation_dict
        except IndexError:
            return None

    def parse_html_for_language_level(self):
        try:
            lang_level_html = re.findall(r'Das Verb gehört zum Wortschatz des Zertifikats Deutsch bzw. zur Stufe [A-Z][0-9]. </span>', self.verb_html)[0]
            lang_level = re.search(
                '%s([A-Z][0-9])%s' % ('Das Verb gehört zum Wortschatz des Zertifikats Deutsch bzw. zur Stufe ',
                              '. </span>'),
                lang_level_html).group(1)
            return lang_level
        except IndexError:
            return None

    def parse_html_for_english_infinitive(self):
        try:
            engl_translation_html = re.findall(r'title="Englisch" alt="Englisch"src="/bedeutungenweb/en.svg" width="13" height="13">&nbsp;</span><span>.*</span>', self.verb_html)[0]
            engl_translation = re.search(
                '%s(.*)%s' % ('title="Englisch" alt="Englisch"src="/bedeutungenweb/en.svg" width="13" height="13">&nbsp;</span><span>',
                              '</span>'),
                engl_translation_html).group(1)
            # currently we just return the first of a list of possible translation, assuming this is the best matching choice
            return engl_translation.split(',')[0]
        except IndexError:
            return None

