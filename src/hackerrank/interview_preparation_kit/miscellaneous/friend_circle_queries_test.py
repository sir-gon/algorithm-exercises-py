import unittest
from .friend_circle_queries import max_circle

TEST_CASES = [
    {
        'title': 'Sample Test case 0',
        'arr': [[1, 2], [1, 3]],
        'answer': [2, 3]
    },
    {
        'title': 'Sample Test case 0',
        'arr': [[1, 2], [1, 3], [1, 2], [1, 3]],
        'answer': [2, 3, 3, 3],
    },
    {
        'title': 'Sample Test case 1',
        'arr': [
            [1000000000, 23],
            [11, 3778],
            [7, 47],
            [11, 1000000000]
        ],
        'answer': [2, 2, 2, 4]
    },
    {
        'title': 'Sample Test case 2',
        'arr': [
            [1, 2],
            [3, 4],
            [1, 3],
            [5, 7],
            [5, 6],
            [7, 4]
        ],
        'answer': [2, 2, 4, 4, 4, 7]
    }
]


class TestFriendCircle(unittest.TestCase):

    def test_max_circle(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                max_circle(_tt['arr']), _tt['answer'],
                f"{_} | max_circle({_tt['arr']}) must be "
                f"=> {_tt['answer']} in {_tt['title']}")
