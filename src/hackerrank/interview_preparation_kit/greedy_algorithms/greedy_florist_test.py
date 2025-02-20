import unittest
from pathlib import Path

from ....lib.loader import loadTestCases
from .greedy_florist import getMinimumCost

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = loadTestCases(
    FILE_PATH + '/greedy_florist.testcases.json')


class TestGreedyFlorist(unittest.TestCase):

    def test_get_minimum_cost(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                getMinimumCost(_tt['k'], _tt['contests']), _tt['expected'],
                f"{_} | getMinimumCost({_tt['k']}, {_tt['contests']}) must be "
                f"=> {_tt['expected']} in {_tt['title']}")
