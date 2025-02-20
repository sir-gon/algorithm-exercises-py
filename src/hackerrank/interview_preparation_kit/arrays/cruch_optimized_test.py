import unittest
from pathlib import Path

from ....hackerrank.lib.loader import load_test_cases
from .cruch_optimized import arrayManipulation

FILE_PATH = str(Path(__file__).resolve().parent)

CRUCH_SMALL_TEST_CASES = load_test_cases(
    FILE_PATH + '/cruch.testcases.json')


class TestCrush(unittest.TestCase):

    def test_array_manipulation_optimized(self):

        for _, _tt in enumerate(CRUCH_SMALL_TEST_CASES):

            self.assertEqual(
                arrayManipulation(_tt['n'], _tt['queries']), _tt['expected'],
                f"{_} | array_manipulation_optimized({_tt['n']}, {_tt['queries']}) "
                f"must be => {_tt['expected']}")
