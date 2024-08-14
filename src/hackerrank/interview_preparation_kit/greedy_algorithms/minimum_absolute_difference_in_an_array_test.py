import unittest
from pathlib import Path

from ....hackerrank.lib.loader import load_test_cases
from .minimum_absolute_difference_in_an_array import minimum_absolute_difference

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = load_test_cases(
    FILE_PATH + '/minimum_absolute_difference_in_an_array.testcases.json')


class TestMinimumAbsoluteDifference(unittest.TestCase):

    def test_minimum_absolute_difference(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                minimum_absolute_difference(_tt['input']), _tt['expected'],
                f"{_} | minimum_absolute_difference({_tt['input']}) must be "
                f"=> {_tt['expected']}")
