# -*- coding: utf-8 -*-

# sentence_generation.py

"""
Computer-assisted language learning: verbforms list generation

Jana Hofmann, Salome Wildermuth
Matrikel-Nr: 17-709-361, 10-289-544
University of Zurich
Institute for Computational Linguistics

- generate sample sentences for given input (here: pronoun + verb)

"""
import random
import re

from transformers import AutoTokenizer, AutoModelWithLMHead, pipeline


class SentenceGenerator:
    def __init__(self):
        checkpoint = "dbmdz/german-gpt2"
        self.tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        self.model = AutoModelWithLMHead.from_pretrained(checkpoint)
        self.valid_sentence = False
        # English sentence generation:

    def generate(self, conjugation_table: list, nr_of_tokens: int = 15):
        while (not self.valid_sentence):
            verbform = random.choice(conjugation_table)
            indx = random.choice(range(0, 1))
            input = verbform[indx].replace('(', '')
            input = input.replace(')', '')
            pipe = pipeline('text-generation', model="dbmdz/german-gpt2",
                            tokenizer="dbmdz/german-gpt2")
            text = pipe(input, max_length=nr_of_tokens)[0]["generated_text"]
            pattern = re.compile(r"[;.!:?]")
            sentence = pattern.split(text)
            sentence_as_list = sentence[0].split(' ')
            print(sentence_as_list)
            if len(sentence_as_list) > 3:
                self.valid_sentence = True
            sentence_as_list[0] = sentence_as_list[0].capitalize()
        return ' '.join(sentence_as_list) + '.'

