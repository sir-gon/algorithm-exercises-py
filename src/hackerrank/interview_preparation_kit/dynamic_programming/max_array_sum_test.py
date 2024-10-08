import unittest
from pathlib import Path

from ....hackerrank.lib.loader import load_test_cases
from .max_array_sum import max_array_sum

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = load_test_cases(
    FILE_PATH + '/max_array_sum.testcases.json')


class TestMaxArraySum(unittest.TestCase):

    def test_max_array_sum(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                max_array_sum(_tt['input']), _tt['expected'],
                f"{_} | max_array_sum({_tt['input']}) must be "
                f"=> {_tt['expected']}")

    def test_max_array_sum_edge_case_zero(self):

        _input = []
        _expected = 0

        self.assertEqual(
            max_array_sum(_input), _expected,
            f"max_array_sum({_input}) must be "
            f"=> {_expected}")

    def test_max_array_sum_edge_case_one(self):

        _input = [1]
        _expected = 1

        self.assertEqual(
            max_array_sum(_input), _expected,
            f"max_array_sum({_input}) must be "
            f"=> {_expected}")
