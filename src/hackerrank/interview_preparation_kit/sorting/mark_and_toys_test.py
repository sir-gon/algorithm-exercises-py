import unittest
from pathlib import Path

from ....lib.loader import loadTestCases
from .mark_and_toys import maximumToys

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = loadTestCases(FILE_PATH + '/mark_and_toys.testcases.json')


class TestMarkAndToys(unittest.TestCase):

    def test_maximum_toys(self):
        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                maximumToys(_tt['prices'], _tt['budget']), _tt['expected'],
                f"{_} | maximumToys({_tt['prices'], _tt['budget']}) must be "
                f"=> {_tt['expected']}")
