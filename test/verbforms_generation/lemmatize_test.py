import unittest

from src.verbforms_generation.verbforms_generation.lemmatize import GermanLemmatizer

lemmatizer = GermanLemmatizer()


class LemmatizeTest(unittest.TestCase):

    def test_lemmatize_verb(self):
        self.assertEqual('sein', lemmatizer.lemmatize('gewesen'))

    def test_lemmatize_ambiguous_verb(self):
        # stahl (Präteritum of stehlen) vs Stahl
        self.assertEqual('stehlen', lemmatizer.lemmatize('stahl'))
