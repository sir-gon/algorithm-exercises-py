import unittest

from .count_triplets_1 import count_triplets

TEST_CASES = [
    {
        'title': 'Sample Test Case 0',
        'input': [1, 2, 2, 4],
        'r': 2,
        'answer': 2
    },
    {
        'title': '',
        'input': [1, 3, 9, 9, 27, 81],
        'r': 3,
        'answer': 6
    },

]


class TestCountTriplets(unittest.TestCase):

    def test_count_triplets(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                count_triplets(_tt['input'], _tt['r']), _tt['answer'],
                f"{_} | count_triplets({_tt['input']}, {_tt['r']}) must be "
                f"=> {_tt['answer']}")
