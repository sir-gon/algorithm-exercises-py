import unittest
from pathlib import Path

from ....lib.loader import loadTestCases
from .recursive_digit_sum import superDigit

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = loadTestCases(
    FILE_PATH + '/recursive_digit_sum.testcases.json')


class TestRecursiveDigitSum(unittest.TestCase):

    def test_super_digit(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                superDigit(_tt['n'], _tt['k']), _tt['expected'],
                f"{_} | superDigit({_tt['n']}, {_tt['k']}) must be "
                f"=> {_tt['expected']} in {_tt['title']}")
