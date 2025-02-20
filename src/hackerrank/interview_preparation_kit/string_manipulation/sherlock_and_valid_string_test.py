import unittest
from pathlib import Path

from ....lib.loader import loadTestCases
from .sherlock_and_valid_string import isValid

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = loadTestCases(FILE_PATH + '/sherlock_and_valid_string.testcases.json')


class TestSherklockAndValidString(unittest.TestCase):

    def test_is_valid(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                isValid(_tt['input']), _tt['expected'],
                f"{_} | isValid({_tt['input']}) must be "
                f"=> {_tt['expected']}")
