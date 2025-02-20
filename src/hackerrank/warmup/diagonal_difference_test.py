import unittest
from .diagonal_difference import diagonalDifference


class TestdiagonalDifference(unittest.TestCase):

    def test_diagonal_difference(self):

        matrix = [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, -12]
        ]

        answer = 15

        self.assertEqual(
            diagonalDifference(matrix), answer,
            f"diagonalDifference({matrix}) must be "
            f"=> {answer}")
