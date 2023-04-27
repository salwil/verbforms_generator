import unittest

from src.verbforms_generation.verbforms_generation.verbforms import Verbforms

verbforms_gehen = Verbforms("geht")
verbforms_sein = Verbforms("seien")
verbforms_kriechen = Verbforms("kriechst")
verbforms_nonverb = Verbforms("Hallo")
verbforms_gewesen = Verbforms("gewesen")
verbforms_stellen = Verbforms("stellen")

class VerbformsTest(unittest.TestCase):

    def test_build_verb_object(self):
        self.assertEqual(verbforms_gehen.verb.infinitive_german, 'gehen')
        self.assertEqual(
            [('ich geh(e)',
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
              'sie gingen ')],
            verbforms_gehen.verb.german_conjugations
        )
        self.assertEqual(verbforms_gehen.verb.language_level, 'A1')

    def test_parse_html_for_infinitive(self):
        self.assertEqual(verbforms_gehen.parse_html_for_german_infinitive(), 'gehen')
        self.assertEqual(verbforms_sein.parse_html_for_german_infinitive(), 'sein')

    def test_parse_html_for_language_level(self):
        self.assertEqual(verbforms_gehen.parse_html_for_language_level(), 'A1')
        self.assertEqual(verbforms_kriechen.parse_html_for_language_level(), 'C2')

    def test_parse_html_for_regularity(self):
        self.assertEqual(False, verbforms_gehen.parse_html_for_regularity())
        self.assertEqual(True, verbforms_stellen.parse_html_for_regularity())

    def test_parse_html_for_english_translation(self):
        self.assertEqual(verbforms_gehen.parse_html_for_english_infinitive(), 'go')
        self.assertEqual(verbforms_sein.parse_html_for_english_infinitive(), 'be')
        self.assertEqual(verbforms_kriechen.parse_html_for_english_infinitive(), 'creep')

    def test_build_verb_object_with_nonverb(self):
        self.assertEqual(verbforms_nonverb.verb, None)
        self.assertEqual(verbforms_gewesen.verb, None)

