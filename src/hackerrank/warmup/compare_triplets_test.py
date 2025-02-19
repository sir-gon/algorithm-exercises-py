import unittest
import pytest
from .compare_triplets import compareTriplets


class TestCompareTriplets(unittest.TestCase):

    def test_compare_triplets_wrong_data(self):

        _a: list[int] = [1]
        _b = [2, 3]

        with pytest.raises(Exception):
            compareTriplets(_a, _b)

        with pytest.raises(Exception):
            compareTriplets([], _b)

        with pytest.raises(Exception):
            compareTriplets(_a, [])

    def test_compare_triplets_test_case0(self):

        tests = [
            {'a': [5, 6, 7], 'b': [3, 6, 10], 'answer': [1, 1]},
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                compareTriplets(_tt['a'], _tt['b']), _tt['answer'],
                f"{_} | compareTriplets({_tt['a']}, {_tt['b']}) must be "
                f"=> {_tt['answer']}")
