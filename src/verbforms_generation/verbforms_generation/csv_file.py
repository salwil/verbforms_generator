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
from pathlib import Path

from src.verbforms_generation.verbforms_generation import helpers
from src.verbforms_generation.verbforms_generation.verb import Verb


class CsvFile:
    def __init__(self):
        self.directory_path = helpers.get_project_path() + '/index_cards'
        if not (os.path.exists(self.directory_path)):
            os.makedirs(self.directory_path)
        self.file_path = self.generate_name()
        self.csvfile = open(self.file_path, 'w')
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

    def convert_verb_forms_to_csv_records(self, verb: Verb):
        # todo: extract list of records for writing into csv-file: [(ich gehe, ich ging), (du gehst, du gingst),...] --> [ich gehe, I go]
        list_of_records = []
        list_of_persons = ['1st pers. sing', '2nd pers. sing', '3rd pers. sing', '1st pers. pl', '2nd pers. pl', '3rd pers. pl']
        # list of timeforms will be dynamic in the future
        list_of_timeforms = ['Präsens', 'Präteritum']
        for verb_person, person in zip(verb.german_conjugations, list_of_persons):
            for time_form, time_name in zip(verb_person, list_of_timeforms):
                list_of_records.append([verb.infinitive_english + ', ' + person + ', ' + time_name, time_form])
        return list_of_records

    def write_record(self, verb: Verb):
        records = self.convert_verb_forms_to_csv_records(verb)
        for record in records:
            self.csv_writer.writerow(record)

    def close_file(self):
        self.csvfile.close()


