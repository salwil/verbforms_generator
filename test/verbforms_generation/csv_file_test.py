import time
import unittest

from src.verbforms_generation.verbforms_generation.csv_file import CsvFile

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
        #self.assertEqual(47, len(self.csv_file_1.file_path))
        self.assertTrue(self.csv_file_1.file_path.endswith('-index-cards.csv'))
        self.assertNotEqual(self.csv_file_1.file_path, self.csv_file_2.file_path)

    def test_write_record(self):
        self.csv_file_1.write_record(["Hello", "World"])
        self.csv_file_2.write_record(["Goodbye", "World"])
        # todo: write assertions

