import unittest
from pathlib import Path

from ....hackerrank.lib.loader import load_test_cases
from .angry_children import maxMin

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = load_test_cases(
    FILE_PATH + '/angry_children.testcases.json')


class TestGreedyFlorist(unittest.TestCase):

    def test_max_min(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                maxMin(_tt['k'], _tt['arr']), _tt['expected'],
                f"{_} | maxMin({_tt['k']}, {_tt['arr']}) must be "
                f"=> {_tt['expected']} in {_tt['title']}")
