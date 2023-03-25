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

from src.verbforms_generation.verbforms_generation.verb import Verb, Praesens, Praeteritum

class CsvFile:
    def __init__(self):
        self.directory_path = self.get_project_path() + '/index_cards'
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

    def write_record(self, record: list):
        self.csv_writer.writerow(record)

    def close_file(self):
        self.csvfile.close()

    def get_project_path(self):
        path = Path(__file__)
        if os.path.dirname(path).endswith('verbforms_generator'):
            return os.path.dirname(path)
        elif os.path.dirname(path.parent).endswith('verbforms_generator'):
            return os.path.dirname(path.parent)
        elif os.path.dirname(path.parent.parent).endswith('verbforms_generator'):
            return os.path.dirname(path.parent.parent)
        elif os.path.dirname(path.parent.parent.parent).endswith('verbforms_generator'):
            return os.path.dirname(path.parent.parent.parent)
        elif os.path.dirname(path.parent.parent.parent.parent).endswith('verbforms_generator'):
            return os.path.dirname(path.parent.parent.parent.parent)
        elif os.path.dirname(path.parent.parent.parent.parent.parent).endswith(
                'verbforms_generator'):
            return os.path.dirname(path.parent.parent.parent.parent.parent)
        elif os.path.dirname(path.parent.parent.parent.parent.parent.parent).endswith(
                'verbforms_generator'):
            return os.path.dirname(path.parent.parent.parent.parent.parent.parent)
        else:
            return os.path.dirname((path))

