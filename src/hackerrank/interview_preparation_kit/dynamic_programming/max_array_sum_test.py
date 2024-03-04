import unittest
from .max_array_sum import max_array_sum

TEST_CASES = [
    {
        'title': 'Sample Test case 0',
        'input': [3, 7, 4, 6, 5],
        'answer': 13
    },
    {
        'title': 'Sample Test case 1',
        'input': [2, 1, 5, 8, 4],
        'answer': 11
    },
    {
        'title': 'Sample Test case 2',
        'input': [3, 5, -7, 8, 10],
        'answer': 15
    }
]


class TestMaxArraySum(unittest.TestCase):

    def test_max_array_sum(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                max_array_sum(_tt['input']), _tt['answer'],
                f"{_} | max_array_sum({_tt['input']}) must be "
                f"=> {_tt['answer']}")

    def test_max_array_sum_edge_case_zero(self):

        _input = []
        _answer = 0

        self.assertEqual(
            max_array_sum(_input), _answer,
            f"max_array_sum({_input}) must be "
            f"=> {_answer}")

    def test_max_array_sum_edge_case_one(self):

        _input = [1]
        _answer = 1

        self.assertEqual(
            max_array_sum(_input), _answer,
            f"max_array_sum({_input}) must be "
            f"=> {_answer}")
