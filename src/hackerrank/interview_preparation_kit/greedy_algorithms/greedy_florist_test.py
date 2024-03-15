import unittest
from .greedy_florist import get_minimum_cost

TEST_CASES = [
    {
        'title': 'Sample Test case 0',
        'k': 3,
        'contests': [2, 5, 6],
        'answer': 13
    },
    {
        'title': 'Sample Test case 1',
        'k': 2,
        'contests': [2, 5, 6],
        'answer': 15
    },
    {
        'title': 'Sample Test case 2',
        'k': 3,
        'contests': [1, 3, 5, 7, 9],
        'answer': 29
    }
]


class TestLuckBalance(unittest.TestCase):

    def test_get_minimum_cost(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                get_minimum_cost(_tt['k'], _tt['contests']), _tt['answer'],
                f"{_} | get_minimum_cost({_tt['k']}, {_tt['contests']}) must be "
                f"=> {_tt['answer']} in {_tt['title']}")
