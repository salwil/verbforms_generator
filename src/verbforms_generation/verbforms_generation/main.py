# -*- coding: utf-8 -*-

# main.py

"""
Computer-assisted language learning: verbforms list generation

Jana Hofmann, Salome Wildermuth
Matrikel-Nr: 17-709-361, 10-289-544
University of Zurich
Institute for Computational Linguistics

- main module for maintaining interaction with user

"""
from .termination_criterion import TerminationCriterionForConversation
import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")

    """
    from src.conversation.conversation.termination_criterion import TerminationCriterionForConversation
    from src.conversation_turn.conversation_turn.turn import ConversationTurn
    from src.conversation.conversation.conversation import Conversation, Language
    """


def main():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        cli = CLI()
        cli.maintain_interaction()


class CLI:
    def __init__(self):
        self.termination_criterion = TerminationCriterionForConversation()


    def maintain_interaction(self):
        turn_number = 1
        print("Please enter a verb in any form, time or mode.")
        while not self.termination_criterion.given():
            verb = input()
            verb = self.__validate(verb)
            print("Please enter the nect verb in any form, time or mode.")


    def __validate(self, user_input):
        while not user_input:
            user_input = input()
        self.termination_criterion.check_user_terminate(user_input)
        return user_input


if __name__ == "__main__":
    main()