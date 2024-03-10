import unittest

from .count_triplets_1 import count_triplets, count_triplets_brute_force

SMALL_TEST_CASES = [
    {
        'title': 'Sample Test Case 0',
        'input': [1, 2, 2, 4],
        'r': 2,
        'answer': 2
    },
    {
        'title': 'Sample Test Case 1',
        'input': [1, 3, 9, 9, 27, 81],
        'r': 3,
        'answer': 6
    },
    {
        'title': 'Sample Test Case 1 (unsorted)',
        'input': [9, 3, 1, 81, 9, 27],
        'r': 3,
        'answer': 1
    },
    {
        'title': 'Sample Test Case 12',
        'input': [1, 5, 5, 25, 125],
        'r': 5,
        'answer': 4
    },
]

TEST_CASES_BIG = [
    {
        'title': 'Sample Test Case 2',
        'input': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'r': 1,
        'answer': 161700
    }
]


class TestCountTriplets(unittest.TestCase):

    def test_count_triplets_brute_force(self):
        for _, _tt in enumerate(SMALL_TEST_CASES):

            self.assertEqual(
                count_triplets_brute_force(_tt['input'], _tt['r']), _tt['answer'],
                f"{_} | count_triplets_brute_force({_tt['input']}, {_tt['r']}) must be "
                f"=> {_tt['answer']}")

    def test_count_triplets(self):

        for _, _tt in enumerate(SMALL_TEST_CASES):

            self.assertEqual(
                count_triplets(_tt['input'], _tt['r']), _tt['answer'],
                f"{_} | count_triplets({_tt['input']}, {_tt['r']}) must be "
                f"=> {_tt['answer']} in {_tt['title']}")

    def test_count_triplets_big_cases(self):

        for _, _tt in enumerate(TEST_CASES_BIG):

            self.assertEqual(
                count_triplets(_tt['input'], _tt['r']), _tt['answer'],
                f"{_} | count_triplets({_tt['input']}, {_tt['r']}) must be "
                f"=> {_tt['answer']} in {_tt['title']}")
