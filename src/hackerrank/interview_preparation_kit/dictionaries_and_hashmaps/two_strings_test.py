import unittest
from pathlib import Path

from ....hackerrank.lib.loader import load_test_cases
from .two_strings import two_strings

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = load_test_cases(
    FILE_PATH + '/two_strings.testcases.json')


class TestTwoStrings(unittest.TestCase):

    def test_two_strings(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                two_strings(_tt['s1'], _tt['s2']), _tt['expected'],
                f"{_} | two_strings({_tt['s1']}, {_tt['s2']}) must be "
                f"=> {_tt['expected']} in {_tt['title']}")
