import unittest

from src.verbforms_generation.verbforms_generation.verb import TimeForm
from src.verbforms_generation.verbforms_generation.verbforms import Verbforms

class VerbformsTest(unittest.TestCase):
    """
    This test class demonstrates how the defined triggers perfectly work for generating a question starting with the
    desired interrogative pronoun.
    Note that the we mock the interrogative pronoun, because in the real method it's chosen on a random base what would
    make it impossible to make meaningful assertions.
    Consequently THIS TEST DOES NOT TEST THE SELECTION OF THE INTERROGATIVE PRONOUN, but the method is tested in
    question_generation_rules_test.py
    """

    def setUp(self) -> None:
        self.verbforms = Verbforms("geht")

    def test_buidl_verb_object(self):
        #self.verbforms.read_html_for_given_verb()
        self.verbforms.parse_html_for_verbforms()
        self.assertEqual(self.verbforms.praesens.infinitive, 'gehen')
        self.assertEqual(self.verbforms.praesens.timeform, TimeForm.PRAESENS)
        self.assertEqual(self.verbforms.praesens.timeform, TimeForm.PRAESENS)
        self.assertEqual(
            self.verbforms.praesens.conjugations,
            {'ich': 'geh(e)', 'du': 'gehst', 'er': 'geht', 'wir': 'geh(e)n', 'ihr': 'geht', 'sie': 'geh(e)n'})


    # todo: add tests per each method

