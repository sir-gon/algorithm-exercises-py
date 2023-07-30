import unittest
import pytest
from .compare_triplets import compare_triplets


class TestCompareTriplets(unittest.TestCase):

    def test_compare_triplets_wrong_data(self):

        _a: list[int] = [1]
        _b = [2, 3]

        with pytest.raises(Exception):
            compare_triplets(_a, _b)

        with pytest.raises(Exception):
            compare_triplets([], _b)

        with pytest.raises(Exception):
            compare_triplets(_a, [])

    def test_compare_triplets_test_case0(self):

        tests = [
          {'a':  [5, 6, 7], 'b': [3, 6, 10], 'answer': [1, 1]},
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                compare_triplets(_tt['a'], _tt['b']), _tt['answer'],
                f"{_} | birthday_cake_candles({_tt['a']}, {_tt['b']}) must be "
                f"=> {_tt['answer']}")
