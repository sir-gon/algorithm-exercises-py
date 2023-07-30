import unittest
import pytest
from .mini_max_sum import mini_max_sum


class TestMiniMaxSum(unittest.TestCase):

    def test_mini_max_sum_wrong_data(self):

        with pytest.raises(Exception):
            mini_max_sum([])

    def test_mini_max_sum(self):

        tests = [
          {'input':  [1, 2, 3, 4, 5], 'answer': '10 14'},
          {'input':  [5, 4, 3, 2, 1], 'answer': '10 14'}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                mini_max_sum(_tt['input']), _tt['answer'],
                f"{_} | miniMaxSum({_tt['input']}) must be "
                f"=> {_tt['answer']}")
