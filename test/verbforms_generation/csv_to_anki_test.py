import unittest

from src.verbforms_generation.verbforms_generation.csv_to_anki import CSVExport


class CSVExportTest(unittest.TestCase):

    def test_base_case(self):
        csv_export = CSVExport('14-05-2023-13-28-52-index-cards.csv')
        csv_export.invoke('createDeck', deck='test1')
        result = csv_export.invoke('deckNames')
        print('got list of decks: {}'.format(result))