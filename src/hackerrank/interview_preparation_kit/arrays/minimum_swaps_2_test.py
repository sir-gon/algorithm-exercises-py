import unittest
from .minimum_swaps_2 import minimum_swaps


class TestMinimumSwaps(unittest.TestCase):

    def test_minimum_swaps(self):

        tests = [
          {'title': 'Sample input 0', 'input': [4, 3, 1, 2], 'answer': 3},
          {'title': 'Sample input 1', 'input': [2, 3, 4, 1, 5], 'answer': 3},
          {'title': 'Sample input 2', 'input': [1, 3, 5, 2, 4, 6, 7], 'answer': 3},
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                minimum_swaps(_tt['input']), _tt['answer'],
                f"{_} | minimum_swaps({_tt['input']}) must be "
                f"=> {_tt['answer']}")
