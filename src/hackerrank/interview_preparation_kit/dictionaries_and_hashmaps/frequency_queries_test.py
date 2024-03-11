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
        'answer': [0, 1]
    }
]


class Test(unittest.TestCase):

    def test_freq_query(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                freq_query(_tt['input']), _tt['answer'],
                f"{_} | freq_query({_tt['input']}) must be "
                f"=> {_tt['answer']}")

    def test_freq_query_edge_case(self):

        self.assertRaisesRegex(ValueError,
                               'Invalid operation',
                               freq_query, [[4, 1]])
