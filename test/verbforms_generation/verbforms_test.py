import unittest

from src.verbforms_generation.verbforms_generation.verb import TimeForm
from src.verbforms_generation.verbforms_generation.verbforms import Verbforms

class VerbformsTest(unittest.TestCase):

    def setUp(self) -> None:
        self.verbforms_gehen = Verbforms("geht")
        self.verbforms_sein = Verbforms("seien")
        self.verbforms_kriechen = Verbforms("kriechst")

    def test_build_verb_object(self):
        #self.verbforms.read_html_for_given_verb()
        self.verbforms_gehen.parse_html_for_verbforms()
        self.assertEqual(self.verbforms_gehen.praesens.infinitive, 'gehen')
        self.assertEqual(self.verbforms_gehen.praesens.timeform, TimeForm.PRAESENS)
        self.assertEqual(self.verbforms_gehen.praesens.timeform, TimeForm.PRAESENS)
        self.assertEqual(
            self.verbforms_gehen.praesens.conjugations,
            {'ich': 'geh(e)', 'du': 'gehst', 'er': 'geht', 'wir': 'geh(e)n', 'ihr': 'geht', 'sie': 'geh(e)n'})
        self.assertEqual(self.verbforms_gehen.praesens.language_level, 'A1')

    def test_parse_html_for_infinitive(self):
        self.assertEqual(self.verbforms_gehen.parse_html_for_infinitive(), 'gehen')
        self.assertEqual(self.verbforms_sein.parse_html_for_infinitive(), 'sein')

    def test_parse_html_for_language_level(self):
        self.assertEqual(self.verbforms_gehen.parse_html_for_language_level(), 'A1')
        self.assertEqual(self.verbforms_kriechen.parse_html_for_language_level(), 'C2')