import unittest

from src.verbforms_generation.verbforms_generation.verb import TimeForm
from src.verbforms_generation.verbforms_generation.verbforms import Verbforms

verbforms_gehen = Verbforms("geht")
verbforms_sein = Verbforms("seien")
verbforms_kriechen = Verbforms("kriechst")

class VerbformsTest(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_build_verb_object(self):
        #self.verbforms.read_html_for_given_verb()
        verbforms_gehen.parse_html_for_verbforms()
        self.assertEqual(verbforms_gehen.praesens.infinitive, 'gehen')
        self.assertEqual(verbforms_gehen.praesens.timeform, TimeForm.PRAESENS)
        self.assertEqual(verbforms_gehen.praesens.timeform, TimeForm.PRAESENS)
        self.assertEqual(
            verbforms_gehen.praesens.conjugations,
            {'ich': 'geh(e)', 'du': 'gehst', 'er': 'geht', 'wir': 'geh(e)n', 'ihr': 'geht', 'sie': 'geh(e)n'})
        self.assertEqual(verbforms_gehen.praesens.language_level, 'A1')

    def test_get_infinitive(self):
        self.assertEqual(verbforms_gehen.get_infinitive(), 'gehen')
        self.assertEqual(verbforms_sein.get_infinitive(), 'sein')

    def test_parse_html_for_language_level(self):
        self.assertEqual(verbforms_gehen.parse_html_for_language_level(), 'A1')
        self.assertEqual(verbforms_kriechen.parse_html_for_language_level(), 'C2')