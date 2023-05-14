# -*- coding: utf-8 -*-

# csv_to_anki.py

"""
Computer-assisted language learning: verbforms list generation

Jana Hofmann, Salome Wildermuth
Matrikel-Nr: 17-709-361, 10-289-544
University of Zurich
Institute for Computational Linguistics

- API to Anki

"""
import json
import urllib.request


class CSVExport:
    def __init__(self, file_path: str):
        self.file_for_export = file_path

    def request(self, action, **params):
        return {'action': action, 'params': params, 'version': 6}

    def invoke(self, action, **params):
        requestJson = json.dumps(self.request(action, **params)).encode('utf-8')
        response = json.load(urllib.request.urlopen(urllib.request.Request('http://localhost:8765', requestJson)))
        if len(response) != 2:
            raise Exception('response has an unexpected number of fields')
        if 'error' not in response:
            raise Exception('response is missing required error field')
        if 'result' not in response:
            raise Exception('response is missing required result field')
        if response['error'] is not None:
            raise Exception(response['error'])
        return response['result']


