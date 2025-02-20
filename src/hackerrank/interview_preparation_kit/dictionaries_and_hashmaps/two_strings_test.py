import unittest
from pathlib import Path

from ....lib.loader import loadTestCases
from .two_strings import twoStrings

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = loadTestCases(
    FILE_PATH + '/two_strings.testcases.json')


class TestTwoStrings(unittest.TestCase):

    def test_two_strings(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                twoStrings(_tt['s1'], _tt['s2']), _tt['expected'],
                f"{_} | twoStrings({_tt['s1']}, {_tt['s2']}) must be "
                f"=> {_tt['expected']} in {_tt['title']}")
