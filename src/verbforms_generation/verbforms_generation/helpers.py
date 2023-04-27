# -*- coding: utf-8 -*-

# verbforms_ui.py

"""
Computer-assisted language learning: verbforms list generation

Jana Hofmann, Salome Wildermuth
Matrikel-Nr: 17-709-361, 10-289-544
University of Zurich
Institute for Computational Linguistics

- helper functions

"""
import csv
import os
from datetime import datetime
from pathlib import Path


def get_project_path():
    path = Path(__file__)
    if os.path.dirname(path).endswith('verbforms_generator'):
        return os.path.dirname(path)
    elif os.path.dirname(path.parent).endswith('verbforms_generator'):
        return os.path.dirname(path.parent)
    elif os.path.dirname(path.parent.parent).endswith('verbforms_generator'):
        return os.path.dirname(path.parent.parent)
    elif os.path.dirname(path.parent.parent.parent).endswith('verbforms_generator'):
        return os.path.dirname(path.parent.parent.parent)
    elif os.path.dirname(path.parent.parent.parent.parent).endswith('verbforms_generator'):
        return os.path.dirname(path.parent.parent.parent.parent)
    elif os.path.dirname(path.parent.parent.parent.parent.parent).endswith(
            'verbforms_generator'):
        return os.path.dirname(path.parent.parent.parent.parent.parent)
    elif os.path.dirname(path.parent.parent.parent.parent.parent.parent).endswith(
            'verbforms_generator'):
        return os.path.dirname(path.parent.parent.parent.parent.parent.parent)
    else:
        return os.path.dirname((path))
