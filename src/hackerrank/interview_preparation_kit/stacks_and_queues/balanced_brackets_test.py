import unittest
from pathlib import Path

from ....lib.loader import loadTestCases
from .balanced_brackets import isBalanced

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = loadTestCases(FILE_PATH + '/balanced_brackets.testcases.json')


class TestBalancedBrackets(unittest.TestCase):

    def test_is_balanced(self):

        for _, testset in enumerate(TEST_CASES):

            for _, _tt in enumerate(testset['tests']):

                self.assertEqual(
                    isBalanced(_tt['input']), _tt['answer'],
                    f"{_} | isBalanced({_tt['input']}) must be "
                    f"=> {_tt['answer']}")
