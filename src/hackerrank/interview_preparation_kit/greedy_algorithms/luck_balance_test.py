import unittest
from pathlib import Path

from ....hackerrank.lib.loader import load_test_cases
from .luck_balance import luckBalance

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = load_test_cases(
    FILE_PATH + '/luck_balance.testcases.json')


class TestLuckBalance(unittest.TestCase):

    def test_luck_balance(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                luckBalance(_tt['k'], _tt['contests']), _tt['expected'],
                f"{_} | luckBalance({_tt['k']}, {_tt['contests']}) must be "
                f"=> {_tt['expected']} in {_tt['title']}")
