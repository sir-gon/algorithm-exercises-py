import unittest
from pathlib import Path

from ....hackerrank.lib.loader import load_test_cases
from .two_d_array import hourglass_sum

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = load_test_cases(
    FILE_PATH + '/two_d_array.testcases.json')


class Test2dArray(unittest.TestCase):

    def test_hourglass_sum(self):
        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                hourglass_sum(_tt['input']), _tt['expected'],
                f"{_} | hourglass_sum({_tt['input']}) must be "
                f"=> {_tt['expected']}")
