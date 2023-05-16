import unittest

from src.verbforms_generation.verbforms_generation.csv_to_anki import CSVExport
import json
import urllib.request

class CSVExportTest(unittest.TestCase):

    def test_base_case(self):
        csv_export = CSVExport('../../index_cards/14-05-2023-13-28-51-index-cards.csv', model_name='Basic')
        csv_export.add_notes()

    def test_can_add_notes(self):
        request_obj = {
            "action": "canAddNotes",
            "version": 6,
            "params": {
                "notes": [
                    {
                        "deckName": "Default",
                        "modelName": "Basic",
                        "fields": {
                            "Front": "front content",
                            "Back": "back content"
                        },
                        "tags": [
                            "yomichan"
                        ]
                    }
                ]
            }
        }

        request_jsonob = json.dumps(request_obj).encode('utf-8')
        response = json.load(urllib.request.urlopen(urllib.request.Request('http://localhost:8765', request_jsonob)))
        print(response)