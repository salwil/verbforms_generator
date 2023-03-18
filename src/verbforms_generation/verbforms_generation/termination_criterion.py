# -*- coding: utf-8 -*-

# termination_criterion.py

"""
Computer-assisted language learning: verbforms list generation

Jana Hofmann, Salome Wildermuth
Matrikel-Nr: 17-709-361, 10-289-544
University of Zurich
Institute for Computational Linguistics

- control if interaction is ongoing or shall be terminated

"""


class TerminationCriterion:
    def __init__(self):
        self.terminate = False

    def given(self):
        return self.terminate


class TerminationCriterionForConversation(TerminationCriterion):

    def check_user_terminate(self, user_input):
        if user_input == 'q!' or user_input == 'quit!':
            self.terminate = True