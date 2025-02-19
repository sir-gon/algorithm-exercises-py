import unittest
from pathlib import Path

from ....hackerrank.lib.loader import load_test_cases
from .count_triplets_1 import countTriplets, countTripletsBruteForce

FILE_PATH = str(Path(__file__).resolve().parent)

SMALL_TEST_CASES = load_test_cases(
    FILE_PATH + '/count_triplets_1.small.testcases.json')

TEST_CASES_BIG = load_test_cases(
    FILE_PATH + '/count_triplets_1.big.testcases.json')


class TestCountTriplets(unittest.TestCase):

    def test_count_triplets_brute_force(self):
        for _, _tt in enumerate(SMALL_TEST_CASES):

            self.assertEqual(
                countTripletsBruteForce(_tt['input'], _tt['r']), _tt['expected'],
                f"{_} | count_triplets_brute_force({_tt['input']}, {_tt['r']}) must be "
                f"=> {_tt['expected']}")

    def test_count_triplets(self):

        for _, _tt in enumerate(SMALL_TEST_CASES):

            self.assertEqual(
                countTriplets(_tt['input'], _tt['r']), _tt['expected'],
                f"{_} | count_triplets({_tt['input']}, {_tt['r']}) must be "
                f"=> {_tt['expected']} in {_tt['title']}")

    def test_count_triplets_big_cases(self):

        for _, _tt in enumerate(TEST_CASES_BIG):

            self.assertEqual(
                countTriplets(_tt['input'], _tt['r']), _tt['expected'],
                f"{_} | count_triplets({_tt['input']}, {_tt['r']}) must be "
                f"=> {_tt['expected']} in {_tt['title']}")
