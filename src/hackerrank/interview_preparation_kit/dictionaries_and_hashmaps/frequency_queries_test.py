import unittest
from pathlib import Path

from ....lib.loader import loadTestCases
from .frequency_queries import freqQuery

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = loadTestCases(
    FILE_PATH + '/frequency_queries.testcases.json')


class TestFreqQuery(unittest.TestCase):

    def test_freq_query(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                freqQuery(_tt['input']), _tt['expected'],
                f"{_} | freqQuery({_tt['input']}) must be "
                f"=> {_tt['expected']}")

    def test_freq_query_edge_case(self):

        self.assertRaisesRegex(ValueError,
                               'Invalid operation',
                               freqQuery, [[4, 1]])
