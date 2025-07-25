import unittest
from pathlib import Path

from ....lib.loader import loadTestCases
from .maximum_xor import maxXor

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = loadTestCases(
    FILE_PATH + '/maximum_xor.testcases.json')


class TestMaximumXor(unittest.TestCase):

    def test_maximum_xor(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                maxXor(_tt['arr'], _tt['queries']), _tt['expected'],
                f"{_} | maxXor({_tt['arr']}, {_tt['queries']}) must be "
                f"=> {_tt['expected']}")
