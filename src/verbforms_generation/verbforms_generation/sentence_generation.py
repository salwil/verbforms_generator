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

from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelWithLMHead, pipeline


class SentenceGenerator:
    def __init__(self):
        checkpoint = "dbmdz/german-gpt2"
        self.tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        self.model = AutoModelWithLMHead.from_pretrained(checkpoint)
        self.valid_sentence = False
        # English sentence generation:
        '''
        checkpoint = "gpt2-large"
        self.tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        self.model = AutoModelForCausalLM.from_pretrained(checkpoint)
        self.pronouns = ['I', 'I', 'You', 'You', 'He', 'She', 'She', 'It', 'We', 'We', 'You', 'They', 'They']
        self.verb_be = {'I': 'am', 'You':'are', 'He': 'is', 'She': 'is', 'It': 'is', 'We':'are', 'They':'are'}
        '''

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

        # English sentence generation:
        '''
        pronoun = random.choice(self.pronouns)
        input = input.replace('to ', '')
        if input == 'be':
            verb_clause = pronoun + ' ' + self.verb_be[pronoun]
        else:
            if pronoun == 'He' or pronoun == 'She' or pronoun == 'It':
                if input.endswith(('a','i','o','u')):
                    verb_clause = pronoun + ' ' + input + 'es'
                elif input.endswith('y'):
                    verb_clause = input.rstrip('y')
                    verb_clause = pronoun + ' ' + verb_clause + 'ies'
                else:
                    verb_clause = pronoun + ' ' + input + 's'
            else:
                verb_clause = pronoun + ' ' + input
        inputs = self.tokenizer(verb_clause, return_tensors="pt")
        #elapsed time with 12 max_tokens: 0:01:14.457686, 20 max_tokens: 0:02:01.105493
        outputs = self.model.generate(**inputs, penalty_alpha=0.6, top_k=4, max_new_tokens=nr_of_tokens)
        out = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
        pattern = re.compile(r"[;.!:]")
        out = pattern.split(out)
        return out[0] + '.'''''
