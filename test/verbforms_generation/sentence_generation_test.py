import unittest
from datetime import datetime

from src.verbforms_generation.verbforms_generation.sentence_generation import SentenceGenerator

generator = SentenceGenerator()


class TranslationTest(unittest.TestCase):

    def test_generate_sentence_for_gehen(self):
        print(generator.generate([('ich geh(e)',
                                   'ich ging',
                                   'ich bin gegangen',
                                   'ich war gegangen',
                                   'ich werde gegangen sein',
                                   'ich werde geh(e)n',
                                   'ich gehe',
                                   'ich ginge'),
                                  ('du gehst',
                                   'du gingst',
                                   'du bist gegangen',
                                   'du warst gegangen',
                                   'du wirst gegangen sein',
                                   'du wirst geh(e)n',
                                   'du gehest',
                                   'du gingest'),
                                  ('er geht',
                                   'er ging',
                                   'er ist gegangen',
                                   'er war gegangen',
                                   'er wird gegangen sein',
                                   'er wird geh(e)n',
                                   'er gehe',
                                   'er ginge'),
                                  ('wir geh(e)n',
                                   'wir gingen',
                                   'wir sind gegangen',
                                   'wir waren gegangen',
                                   'wir werden gegangen sein',
                                   'wir werden geh(e)n',
                                   'wir geh(e)n',
                                   'wir gingen'),
                                  ('ihr geht',
                                   'ihr gingt',
                                   'ihr seid gegangen',
                                   'ihr wart gegangen',
                                   'ihr werdet gegangen sein',
                                   'ihr werdet geh(e)n',
                                   'ihr gehet',
                                   'ihr ginget'),
                                  ('sie geh(e)n',
                                   'sie gingen',
                                   'sie sind gegangen',
                                   'sie waren gegangen',
                                   'sie werden gegangen sein',
                                   'sie werden geh(e)n ',
                                   'sie geh(e)n ',
                                   'sie gingen ')]))
