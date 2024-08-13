import unittest
from pathlib import Path

from ....hackerrank.lib.loader import load_test_cases
from .frequency_queries import freq_query

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = load_test_cases(
    FILE_PATH + '/frequency_queries.testcases.json')


class TestFreqQuery(unittest.TestCase):

    def test_freq_query(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                freq_query(_tt['input']), _tt['expected'],
                f"{_} | freq_query({_tt['input']}) must be "
                f"=> {_tt['expected']}")

    def test_freq_query_edge_case(self):

        self.assertRaisesRegex(ValueError,
                               'Invalid operation',
                               freq_query, [[4, 1]])
