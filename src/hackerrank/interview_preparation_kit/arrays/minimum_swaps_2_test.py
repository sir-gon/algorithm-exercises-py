import unittest
from pathlib import Path

from ....lib.loader import loadTestCases
from .minimum_swaps_2 import minimumSwaps

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = loadTestCases(
    FILE_PATH + '/minimum_swaps_2.testcases.json')


class TestMinimumSwaps(unittest.TestCase):

    def test_minimum_swaps(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                minimumSwaps(_tt['input']), _tt['expected'],
                f"{_} | minimumSwaps({_tt['input']}) must be "
                f"=> {_tt['expected']}")
