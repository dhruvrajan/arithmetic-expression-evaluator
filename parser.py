__author__ = 'dhruv'

import string
import re
import operator

operations = {"+": operator.add, "*": operator.mul}

class Parser():
    """ Parser for Arithmetic Expressions, using Dijkstra's Two-Stack Algorithm"""

    def __init__(self):
        self.operator_stack = []
        self.value_stack = []

    def parse(self, s: str):
        s = s.replace(" ", "").replace("(", "")
        iterator = self.string_iterator(s)
        while True:
            try:
                value = next(iterator)
            except StopIteration:
                break

            if value in operations.keys():
                self.operator_stack.append(operations[value])

            elif value.isdigit():
                # Assume only integer values

    @staticmethod
    def string_iterator(s: str):
        return iter(list(s))
