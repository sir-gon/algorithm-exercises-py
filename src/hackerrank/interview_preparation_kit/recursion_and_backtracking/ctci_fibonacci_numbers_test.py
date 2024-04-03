import unittest
from .ctci_fibonacci_numbers import fibonacci

TEST_CASES = [
    {
        'title': 'Sample Test case 0',
        'input': 5,
        'answer': 5
    },
    {
        'title': 'Sample Test case 1',
        'input': 12,
        'answer': 144,
    },
    {
        'title': 'Sample Test case 2',
        'input': 17,
        'answer': 1597
    }
]


class TestRecursionFibonacciNumbers(unittest.TestCase):

    def test_fibonacci(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                fibonacci(_tt['input']), _tt['answer'],
                f"{_} | fibonacci({_tt['input']}) must be "
                f"=> {_tt['answer']} in {_tt['title']}")
