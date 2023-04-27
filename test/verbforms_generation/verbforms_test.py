import unittest

from src.verbforms_generation.verbforms_generation.lemmatize import GermanLemmatizer
from src.verbforms_generation.verbforms_generation.verbforms import Verbforms

lemmatizer = GermanLemmatizer()

verbforms_gehen = Verbforms("geht", lemmatizer)
verbforms_sein = Verbforms("seien", lemmatizer)
verbforms_stellen = Verbforms("stellen", lemmatizer)


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
        verbforms_kriechen = Verbforms("kriechst", lemmatizer)
        self.assertEqual(verbforms_kriechen.parse_html_for_language_level(), 'C2')

    def test_parse_html_for_regularity(self):
        self.assertEqual(False, verbforms_gehen.parse_html_for_regularity())
        self.assertEqual(True, verbforms_stellen.parse_html_for_regularity())

    def test_parse_html_for_english_translation(self):
        verbforms_komplementieren = Verbforms("komplementieren", lemmatizer)
        self.assertEqual('go, walk, went, leave, sell', verbforms_gehen.parse_html_for_english_infinitive())
        self.assertEqual('be, stay, exist, been, be (of) opinion',
                         verbforms_sein.parse_html_for_english_infinitive(), 'be')
        self.assertEqual('complement', verbforms_komplementieren.parse_html_for_english_infinitive())

    def test_build_verb_object_with_nonverb(self):
        verbforms_nonverb = Verbforms("Hallo", lemmatizer)
        self.assertEqual(None, verbforms_nonverb.verb)

    def test_input_that_needs_lemmatization(self):
        verbforms_gewesen = Verbforms("gewesen", lemmatizer)
        self.assertEqual('sein', verbforms_gewesen.verb.infinitive_german)
        self.assertEqual('be, stay, exist, been, be (of) opinion', verbforms_gewesen.verb.infinitive_english)
        self.assertEqual('A1', verbforms_gewesen.verb.language_level)
