import unittest
from pathlib import Path

from ....hackerrank.lib.loader import load_test_cases
from .greedy_florist import getMinimumCost

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = load_test_cases(
    FILE_PATH + '/greedy_florist.testcases.json')


class TestGreedyFlorist(unittest.TestCase):

    def test_get_minimum_cost(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                getMinimumCost(_tt['k'], _tt['contests']), _tt['expected'],
                f"{_} | getMinimumCost({_tt['k']}, {_tt['contests']}) must be "
                f"=> {_tt['expected']} in {_tt['title']}")
