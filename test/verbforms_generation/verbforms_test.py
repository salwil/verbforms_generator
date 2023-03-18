import unittest
from unittest.mock import patch, MagicMock
from src.verbforms_generation.verbforms_generation import verbforms

class Verbforms(unittest.TestCase):
    """
    This test class demonstrates how the defined triggers perfectly work for generating a question starting with the
    desired interrogative pronoun.
    Note that the we mock the interrogative pronoun, because in the real method it's chosen on a random base what would
    make it impossible to make meaningful assertions.
    Consequently THIS TEST DOES NOT TEST THE SELECTION OF THE INTERROGATIVE PRONOUN, but the method is tested in
    question_generation_rules_test.py
    """

    def setUp(self) -> None:
        self.verbforms = verbforms.Verbforms("geht")

    def test_read_html_for_given_verb(self):
        self.verbforms.read_html_for_given_verb()
        # todo: add assertions

