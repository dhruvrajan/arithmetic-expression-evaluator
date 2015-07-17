__author__ = 'dhruv'

import unittest
from parser import Parser
from unittest import TestCase

class TestParser(TestCase):

    expression = "(1 + (2 + 3))"

    def test_parser(self):
        parser = Parser()
        parser.parse(self.expression)

if __name__ == "__main__":
    unittest.main()