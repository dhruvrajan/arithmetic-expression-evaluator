__author__ = 'dhruv'

import unittest
from parser import Parser
from unittest import TestCase
import operator
operations = {"+": operator.add, "*": operator.mul, "-": operator.sub,
              "/": operator.truediv}
class TestParser(TestCase):

    # expression = "(((1 + (2 + (3 * (7 + 8))))/6) - 1)"
    expression = "(1 + ((2 * (4/6)) + 3))"

    def test_parser(self):
        parser = Parser()
        print(parser.parse(self.expression))

if __name__ == "__main__":
    unittest.main()