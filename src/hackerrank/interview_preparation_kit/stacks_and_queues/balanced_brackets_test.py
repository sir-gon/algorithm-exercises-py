import unittest
from pathlib import Path

from ....hackerrank.lib.loader import load_test_cases
from .balanced_brackets import is_balanced

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = load_test_cases(FILE_PATH + '/balanced_brackets.testcases.json')


class TestBalancedBrackets(unittest.TestCase):

    def test_is_balanced(self):

        for _, testset in enumerate(TEST_CASES):

            for _, _tt in enumerate(testset['tests']):

                self.assertEqual(
                    is_balanced(_tt['input']), _tt['answer'],
                    f"{_} | is_balanced({_tt['input']}) must be "
                    f"=> {_tt['answer']}")
