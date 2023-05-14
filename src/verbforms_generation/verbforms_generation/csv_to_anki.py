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

    def invoke_with_json(self, request_json_object):
        """ updated function to use directly an json formatted object, generated by param_creator function , instead of a classical python dict"""
        requestJsonob = json.dumps(request_json_object).encode('utf-8')
        #print(requestJsonob)
        response = json.load(urllib.request.urlopen(urllib.request.Request('http://localhost:8765', requestJsonob)))
        print(response)
        if len(response) != 2:
            raise Exception('response has an unexpected number of fields')
        if 'error' not in response:
            raise Exception('response is missing required error field')
        if 'result' not in response:
            raise Exception('response is missing required result field')
        if response['error'] is not None:
            raise Exception(response['error'])


        return response['result']

    def create_note(self, deckName, modelName, front, back):
        """ creates the object for a single note (card) in anki, all params MUST be specified, otherwise it does not work"""
        note = {
            "deckName": deckName,
            "modelName": modelName,
            "fields": {
                "Front": "{}".format(front),
                "Back": "{}".format(back)
            }
        }
        #print("iam the note", note)
        return note

    def create_param(self, action, version, deckName, modelName, csvfile):
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
            for row in reader:
                #print(row)
                #print("iam the dic",obj["params"]["notes"])
                obj["params"]["notes"].append(self.create_note(deckName, modelName, front=row[0], back=row[1]))
        #print(obj)
        return obj

    def add_notes(self, deckName="verbforms2", action="addNotes", version= 6,  modelName="Basic"):
        """wrapping function to generate new anki cards directly form a CSVfile"""
        try:
            self.invoke('createDeck', deck=deckName)
            add_notes_request_body = self.create_param(action=action, version=version, deckName=deckName, modelName=modelName,
                                                     csvfile=self.file_for_export)
            print(add_notes_request_body)
            self.invoke_with_json(add_notes_request_body)
        except urllib.error.URLError:
            print("Could not connect to anki server, please make sure anki is open")
