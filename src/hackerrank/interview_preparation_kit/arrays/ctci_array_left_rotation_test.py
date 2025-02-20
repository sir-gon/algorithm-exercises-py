import unittest
from pathlib import Path

from ....hackerrank.lib.loader import load_test_cases
from .ctci_array_left_rotation import rotLeft, rotLeftOne

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = load_test_cases(
    FILE_PATH + '/ctci_array_left_rotation.testcases.json')


class TestArrayLeftRotation(unittest.TestCase):

    def test_rot_left_one(self):
        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                rotLeftOne(_tt['input']), _tt['expected'],
                f"{_} | rotLeftOne({_tt['input']}) must be "
                f"=> {_tt['expected']}")

    def test_rot_left(self):

        tests = [
            {'input': [1, 2, 3, 4, 5], 'd': 4, 'expected': [5, 1, 2, 3, 4]},
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                rotLeft(_tt['input'], _tt['d']), _tt['expected'],
                f"{_} | rotLeft({_tt['input']}) must be "
                f"=> {_tt['expected']}")
