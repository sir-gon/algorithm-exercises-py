import unittest
from .maximum_xor import max_xor

TEST_CASES = [
    {
        'title': 'Sample Test case 0',
        'arr': [0, 1, 2],
        'queries': [3, 7, 2],
        'answer': [3, 7, 3]
    }
]


class TestMaximumXor(unittest.TestCase):

    def test_max_xor(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                max_xor(_tt['arr'], _tt['queries']), _tt['answer'],
                f"{_} | max_xor({_tt['arr']}, {_tt['queries']}) must be "
                f"=> {_tt['answer']}")
