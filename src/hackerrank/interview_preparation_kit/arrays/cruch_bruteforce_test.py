import unittest
from pathlib import Path

from ....lib.loader import loadTestCases
from .cruch_bruteforce import arrayManipulation

FILE_PATH = str(Path(__file__).resolve().parent)

CRUCH_SMALL_TEST_CASES = loadTestCases(
    FILE_PATH + '/cruch.testcases.json')


class TestCruchBruteForce(unittest.TestCase):

    def test_array_manipulation(self):

        for _, _tt in enumerate(CRUCH_SMALL_TEST_CASES):

            self.assertEqual(
                arrayManipulation(_tt['n'], _tt['queries']), _tt['expected'],
                f"{_} | arrayManipulation({_tt['n']}, {_tt['queries']}) must be "
                f"=> {_tt['expected']}")
