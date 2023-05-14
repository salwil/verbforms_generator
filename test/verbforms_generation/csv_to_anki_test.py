import unittest

from src.verbforms_generation.verbforms_generation.csv_to_anki import CSVExport


class CSVExportTest(unittest.TestCase):

    def test_base_case(self):
        csv_export = CSVExport('../../index_cards/14-05-2023-13-28-52-index-cards.csv')
        csv_export.add_notes()