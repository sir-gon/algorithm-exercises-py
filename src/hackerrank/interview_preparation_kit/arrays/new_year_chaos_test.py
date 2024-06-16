import unittest
from .new_year_chaos import minimum_bribes_transform, TOO_CHAOTIC_ERROR


class TestMinimumBribes(unittest.TestCase):

    def test_minimum_bribes(self):

        tests = [
            {'title': "Test Case 0-0",
                'input': [2, 1, 5, 3, 4], 'answer': 3},
            {'title': "Test Case 0-1",
                'input': [2, 5, 1, 3, 4], 'answer': TOO_CHAOTIC_ERROR},
            {'title': "Test Case 1-1",
                'input': [5, 1, 2, 3, 7, 8, 6, 4], 'answer': TOO_CHAOTIC_ERROR},
            {'title': "Test Case 1-2",
                'input': [1, 2, 5, 3, 7, 8, 6, 4], 'answer': 7},
            {'title': "Test Case 2",
                'input': [1, 2, 5, 3, 4, 7, 8, 6], 'answer': 4},
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                minimum_bribes_transform(_tt['input']), _tt['answer'],
                f"{_} | minimum_bribes_transform({_tt['input']}) must be "
                f"=> {_tt['answer']}")
