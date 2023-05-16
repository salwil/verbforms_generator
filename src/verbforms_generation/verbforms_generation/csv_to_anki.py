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
import csv
import json
import urllib.request


class CSVExport:
    def __init__(self, file_path: str, model_name: str):
        self.file_for_export = file_path
        self.model_name = model_name

    #def request(self, action, **params):
    #    return {"action": action, "params": params, "version": 2}

    def invoke(self, action, **params):
        request_json = json.dumps(self.request(action, **params)).encode('utf-8')
        response = json.load(urllib.request.urlopen(urllib.request.Request('http://localhost:8765', request_json)))
        if len(response) != 2:
            raise Exception('response has an unexpected number of fields')
        if 'error' not in response:
            raise Exception('response is missing required error field')
        if 'result' not in response:
            raise Exception('response is missing required result field')
        if response['error'] is not None:
            raise Exception(response['error'])
        return response['result']

    def invoke_with_json(self, request_json_object):
        request_jsonob = json.dumps(request_json_object).encode('utf-8')
        response = json.load(urllib.request.urlopen(urllib.request.Request('http://localhost:8765', request_jsonob)))
        print(response)
        '''
        if len(response) != 2:
            raise Exception('response has an unexpected number of fields')
        if 'error' not in response:
            raise Exception('response is missing required error field')
        if 'result' not in response:
            raise Exception('response is missing required result field')
        if response['error'] is not None:
            raise Exception(response['error'])'''

        #return response['result']
        return response

    def create_note(self, deck_name, model_name, card_id, front, back):
        """ creates the object for a single note (card) in anki, all params MUST be specified, otherwise it does not work"""
        note = {
            "deckName": deck_name,
            "modelName": model_name,
            "fields": {
                "Front": "{}".format(front),
                "Back": "{}".format(back),
                "Card ID": "{}".format(card_id)
            },
            "tags": ["yomichan"]
        }
        return note

    def create_param(self, action, version, deck_name, model_name, csvfile):
        """ creates the whole object to give the invokejson function"""
        obj = {
            "action": action,
            "version": version,
            "params": {
                "notes": []
            }
        }
        with open(csvfile) as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            card_id = 0
            for row in reader:
                obj["params"]["notes"].append(self.create_note(deck_name, model_name, card_id, front=row[0], back=row[1]))
                card_id += 1
        print(obj)
        return obj

    def add_notes(self, deck_name="verbforms4", action="addNotes", version=6):
        """wrapping function to generate new anki cards directly form a CSVfile"""
        try:
            #self.invoke('createDeck', deck=deck_name)
            add_notes_request_body = self.create_param(action=action, version=version, deck_name=deck_name,
                                                       model_name=self.model_name,
                                                       csvfile=self.file_for_export)
            print(add_notes_request_body)
            self.invoke_with_json(add_notes_request_body)
        except urllib.error.URLError:
            print("Could not connect to anki server, please make sure anki is open")
