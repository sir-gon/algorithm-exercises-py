import unittest
from pathlib import Path

from ....lib.loader import loadTestCases
from .ctci_fibonacci_numbers import fibonacci

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = loadTestCases(
    FILE_PATH + '/ctci_fibonacci_numbers.testcases.json')


class TestRecursionFibonacciNumbers(unittest.TestCase):

    def test_fibonacci(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                fibonacci(_tt['input']), _tt['expected'],
                f"{_} | fibonacci({_tt['input']}) must be "
                f"=> {_tt['expected']} in {_tt['title']}")
