import unittest

from src.verbforms_generation.verbforms_generation.verbforms import Verbforms

class VerbformsTest(unittest.TestCase):

    def setUp(self) -> None:
        self.verbforms_gehen = Verbforms("geht")
        self.verbforms_sein = Verbforms("seien")
        self.verbforms_kriechen = Verbforms("kriechst")
        self.verbforms_nonverb = Verbforms("Hallo")

    def test_build_verb_object(self):
        self.assertEqual(self.verbforms_gehen.verb.infinitive_german, 'gehen')
        self.assertEqual(
            [('ich geh(e)',
              'ich ging',
              'ich bin gegangen',
              'ich war gegangen',
              'ich werde gegangen sein',
              'ich werde geh(e)n'),
             ('du gehst',
              'du gingst',
              'du bist gegangen',
              'du warst gegangen',
              'du wirst gegangen sein',
              'du wirst geh(e)n'),
             ('er geht',
              'er ging',
              'er ist gegangen',
              'er war gegangen',
              'er wird gegangen sein',
              'er wird geh(e)n'),
             ('wir geh(e)n',
              'wir gingen',
              'wir sind gegangen',
              'wir waren gegangen',
              'wir werden gegangen sein',
              'wir werden geh(e)n'),
             ('ihr geht',
              'ihr gingt',
              'ihr seid gegangen',
              'ihr wart gegangen',
              'ihr werdet gegangen sein',
              'ihr werdet geh(e)n'),
             ('sie geh(e)n',
              'sie gingen',
              'sie sind gegangen',
              'sie waren gegangen',
              'sie werden gegangen sein',
              'sie werden geh(e)n ')],
            self.verbforms_gehen.verb.german_conjugations
        )
        self.assertEqual(self.verbforms_gehen.verb.language_level, 'A1')

    def test_parse_html_for_infinitive(self):
        self.assertEqual(self.verbforms_gehen.parse_html_for_german_infinitive(), 'gehen')
        self.assertEqual(self.verbforms_sein.parse_html_for_german_infinitive(), 'sein')

    def test_parse_html_for_language_level(self):
        self.assertEqual(self.verbforms_gehen.parse_html_for_language_level(), 'A1')
        self.assertEqual(self.verbforms_kriechen.parse_html_for_language_level(), 'C2')

    def test_parse_html_for_english_translation(self):
        self.assertEqual(self.verbforms_gehen.parse_html_for_english_infinitive(), 'go')
        self.assertEqual(self.verbforms_sein.parse_html_for_english_infinitive(), 'be')
        self.assertEqual(self.verbforms_kriechen.parse_html_for_english_infinitive(), 'creep')

    def test_build_verb_object_with_nonverb(self):
        self.assertEqual(self.verbforms_nonverb.verb, None)
