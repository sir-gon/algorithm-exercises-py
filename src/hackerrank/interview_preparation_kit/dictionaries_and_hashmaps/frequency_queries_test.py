import unittest

from .frequency_queries import freq_query

TEST_CASES = [
    {
        'title': 'Sample Test Case 0',
        'input': [
            [1, 5],
            [1, 6],
            [3, 2],
            [1, 10],
            [1, 10],
            [1, 6],
            [2, 5],
            [3, 2]
        ],
        'expected': [0, 1]
    },
    {
        'title': 'Sample Test Case 2',
        'input': [
            [1, 3],
            [2, 3],
            [3, 2],
            [1, 4],
            [1, 5],
            [1, 5],
            [1, 4],
            [3, 2],
            [2, 4],
            [3, 2]
        ],
        'expected': [0, 1, 1]
    },
    {
        'title': 'Sample Test Case 3',
        'input': [
            [1, 3],
            [1, 38],
            [2, 1],
            [1, 16],
            [2, 1],
            [2, 2],
            [1, 64],
            [1, 84],
            [3, 1],
            [1, 100],
            [1, 10],
            [2, 2],
            [2, 1],
            [1, 67],
            [2, 2],
            [3, 1],
            [1, 99],
            [1, 32],
            [1, 58],
            [3, 2]
        ],
        'expected': [1, 1, 0]
    },
    {
        'title': 'Sample Test Case 3',
        'input': [
            [1, 3],
            [1, 38],
            [2, 1],
            [1, 16],
            [2, 1],
            [2, 2],
            [1, 64],
            [1, 84],
            [3, 1],
            [1, 100],
            [1, 10],
            [2, 2],
            [2, 1],
            [1, 67],
            [2, 2],
            [3, 1],
            [1, 99],
            [1, 32],
            [1, 58],
            [3, 2]
        ],
        'expected': [1, 1, 0]
    }
]


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
