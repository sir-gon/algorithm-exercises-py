import unittest
from .luck_balance import luck_balance

TEST_CASES = [
    {
        'title': 'Sample Test case 0',
        'k': 3,
        'contests': [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]],
        'answer': 29
    }
]


class TestLuckBalance(unittest.TestCase):

    def test_luck_balance(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                luck_balance(_tt['k'], _tt['contests']), _tt['answer'],
                f"{_} | luck_balance({_tt['k']}, {_tt['contests']}) must be "
                f"=> {_tt['answer']} in {_tt['title']}")
