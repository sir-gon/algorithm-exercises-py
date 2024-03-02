import unittest
from .minimum_absolute_difference_in_an_array import minimum_absolute_difference

TEST_CASES = [
    {
        'title': 'Sample Test case 0',
        'input': [3, -7, 0],
        'answer': 3
    },
    {
        'title': 'Sample Test case 1',
        'input': [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75],
        'answer': 1
    },
    {
        'title': 'Sample Test case 2',
        'input': [1, -3, 71, 68, 17],
        'answer': 3
    }
]


class TestMakeAnagramt(unittest.TestCase):

    def test_minimum_absolute_difference(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                minimum_absolute_difference(_tt['input']), _tt['answer'],
                f"{_} | minimum_absolute_difference({_tt['input']}) must be "
                f"=> {_tt['answer']}")
