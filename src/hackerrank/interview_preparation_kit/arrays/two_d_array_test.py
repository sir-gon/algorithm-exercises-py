import unittest
from pathlib import Path

from ....lib.loader import loadTestCases
from .two_d_array import hourglassSum

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = loadTestCases(
    FILE_PATH + '/two_d_array.testcases.json')


class Test2dArray(unittest.TestCase):

    def test_hourglass_sum(self):
        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                hourglassSum(_tt['input']), _tt['expected'],
                f"{_} | hourglassSum({_tt['input']}) must be "
                f"=> {_tt['expected']}")
