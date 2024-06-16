import unittest
from .angry_children import max_min

TEST_CASES = [
    {
        'title': 'Sample Test case 0',
        'k': 3,
        'arr': [10, 100, 300, 200, 1000, 20, 30],
        'answer': 20
    },
    {
        'title': 'Sample Test case 1',
        'k': 4,
        'arr': [1, 2, 3, 4, 10, 20, 30, 40, 100, 200],
        'answer': 3
    },
    {
        'title': 'Sample Test case 2',
        'k': 2,
        'arr': [1, 2, 1, 2, 1],
        'answer': 0
    },
    {
        'title': 'Sample Test case 16',
        'k': 3,
        'arr': [100, 200, 300, 350, 400, 401, 402],
        'answer': 2
    }

]


class TestGreedyFlorist(unittest.TestCase):

    def test_max_min(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                max_min(_tt['k'], _tt['arr']), _tt['answer'],
                f"{_} | max_min({_tt['k']}, {_tt['arr']}) must be "
                f"=> {_tt['answer']} in {_tt['title']}")
