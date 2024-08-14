import unittest
from pathlib import Path

from ....hackerrank.lib.loader import load_test_cases
from .minimum_swaps_2 import minimum_swaps

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = load_test_cases(
    FILE_PATH + '/minimum_swaps_2.testcases.json')


class TestMinimumSwaps(unittest.TestCase):

    def test_minimum_swaps(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                minimum_swaps(_tt['input']), _tt['expected'],
                f"{_} | minimum_swaps({_tt['input']}) must be "
                f"=> {_tt['expected']}")
