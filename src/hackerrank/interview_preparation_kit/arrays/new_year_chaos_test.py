import unittest
from pathlib import Path

from ....hackerrank.lib.loader import load_test_cases
from .new_year_chaos import minimumBribes, minimumBribesText

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = load_test_cases(
    FILE_PATH + '/new_year_chaos.testcases.json')


class TestMinimumBribes(unittest.TestCase):

    def test_minimum_bribes(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                minimumBribesText(_tt['input']), _tt['expected'],
                f"{_} | minimumBribesText({_tt['input']}) must be "
                f"=> {_tt['expected']}")

            minimumBribes(_tt['input'])  # Print the result (for coverage)
