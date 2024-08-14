import unittest
from pathlib import Path

from ....hackerrank.lib.loader import load_test_cases
from .sherlock_and_valid_string import is_valid

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = load_test_cases(FILE_PATH + '/sherlock_and_valid_string.testcases.json')


class TestSherklockAndValidString(unittest.TestCase):

    def test_is_valid(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                is_valid(_tt['input']), _tt['expected'],
                f"{_} | is_valid({_tt['input']}) must be "
                f"=> {_tt['expected']}")
