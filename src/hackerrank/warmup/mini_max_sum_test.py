import unittest
import pytest
from .mini_max_sum import miniMaxSum


class TestMiniMaxSum(unittest.TestCase):

    def test_mini_max_sum_wrong_data(self):

        with pytest.raises(Exception):
            miniMaxSum([])

    def test_mini_max_sum(self):

        tests = [
            {'input': [1, 2, 3, 4, 5], 'answer': '10 14'},
            {'input': [5, 4, 3, 2, 1], 'answer': '10 14'}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                miniMaxSum(_tt['input']), _tt['answer'],
                f"{_} | miniMaxSum({_tt['input']}) must be "
                f"=> {_tt['answer']}")
