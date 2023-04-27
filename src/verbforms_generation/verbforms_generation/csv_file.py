# -*- coding: utf-8 -*-

# verbforms_ui.py

"""
Computer-assisted language learning: verbforms list generation

Jana Hofmann, Salome Wildermuth
Matrikel-Nr: 17-709-361, 10-289-544
University of Zurich
Institute for Computational Linguistics

- all that is needed for the csv file handling

"""
import csv
import os
from datetime import datetime

from src.verbforms_generation.verbforms_generation import helpers
from src.verbforms_generation.verbforms_generation.verb import Verb


class CsvFile:
    def __init__(self):
        self.directory_path = helpers.get_project_path() + '/index_cards'
        if not (os.path.exists(self.directory_path)):
            os.makedirs(self.directory_path)
        self.file_path = self.generate_name()
        self.is_open = None
        self.csvfile = self.open_file()
        self.csv_writer = csv.writer(self.csvfile, delimiter = '\t', quotechar='"')

    def generate_name (self):
        return self.directory_path \
               + '/'\
               + datetime\
                   .today()\
                   .strftime("%d-%m-%Y-") \
               + datetime\
                   .time(datetime.now())\
                   .strftime("%H-%M-%S") \
               + '-index-cards.csv'

    def convert_verb_forms_to_csv_records(self, verb: Verb, list_of_timeforms: list):
        # todo: extract list of records for writing into csv-file: [(ich gehe, ich ging), (du gehst, du gingst),...] --> [ich gehe, I go]
        list_of_records = []
        list_of_persons = ['1st pers. sing', '2nd pers. sing', '3rd pers. sing', '1st pers. pl', '2nd pers. pl', '3rd pers. pl']
        # current list of timeforms in verbforms.py: ['Präsens', 'Präteritum', 'Perfekt', 'Plusquamperfekt', 'Futur I', 'Futur II']
        time_form_names = ['Präsens',
                           'Präteritum',
                           #'Imperativ',
                           #'Konjunktiv I',
                           #'Konjunktiv II',
                           'Perfekt',
                           'Plusquamperfekt',
                           'Futur II',
                           'Futur I' ]
        # list of timeforms will be dynamic in the future
        for verb_person, person in zip(verb.german_conjugations, list_of_persons):
            for time_form_verb, time_form, time_form_name in zip(verb_person, list_of_timeforms, time_form_names):
                if time_form:
                    list_of_records.append([verb.infinitive_english + ', ' + person + ', ' + time_form_name, time_form_verb])
                else:
                    pass
        return list_of_records

    def write_record(self, verb: Verb, list_of_timeforms: list):
        records = self.convert_verb_forms_to_csv_records(verb, list_of_timeforms)
        for record in records:
            self.csv_writer.writerow(record)

    def open_file(self):
        self.is_open = True
        return open(self.file_path, 'w')

    def close_file(self):
        self.csvfile.close()
        self.is_open = False


