import time
import unittest

from src.verbforms_generation.verbforms_generation.csv_file import CsvFile
from src.verbforms_generation.verbforms_generation.verb import Verb


class VerbformsTest(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_file_1 = CsvFile()
        # file name uniqueness bases on date / timestamp
        time.sleep(1)
        self.csv_file_2 = CsvFile()

    def tearDown(self) -> None:
        self.csv_file_1.close_file()
        self.csv_file_2.close_file()

    def test_generate_name(self):
        print(self.csv_file_1.file_path)
        print(self.csv_file_2.file_path)
        self.assertTrue(self.csv_file_1.file_path.endswith('-index-cards.csv'))
        self.assertNotEqual(self.csv_file_1.file_path, self.csv_file_2.file_path)

    def test_write_record(self):
        conjugation_table = [('ich gehe', 'ich ging'),
                             ('du gehst', 'du gingst'),
                             ('sie geht', 'sie ging'),
                             ('wir gehen', 'wir gingen'),
                             ('ihr geht', 'ihr gingt'),
                             ('sie gehen', 'sie gingen')]
        verb = Verb('gehen', 'go', conjugation_table, 'A1')
        list_of_timeforms = [True, False, True, False, False, False, False, False, False]
        self.csv_file_1.write_record(verb, list_of_timeforms)
        # todo: write assertions, currently manual verification of file content needed
