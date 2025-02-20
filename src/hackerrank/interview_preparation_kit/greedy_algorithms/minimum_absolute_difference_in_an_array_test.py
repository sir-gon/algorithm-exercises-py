import unittest
from pathlib import Path

from ....lib.loader import loadTestCases
from .minimum_absolute_difference_in_an_array import minimumAbsoluteDifference

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = loadTestCases(
    FILE_PATH + '/minimum_absolute_difference_in_an_array.testcases.json')


class TestMinimumAbsoluteDifference(unittest.TestCase):

    def test_minimum_absolute_difference(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                minimumAbsoluteDifference(_tt['input']), _tt['expected'],
                f"{_} | minimumAbsoluteDifference({_tt['input']}) must be "
                f"=> {_tt['expected']}")
