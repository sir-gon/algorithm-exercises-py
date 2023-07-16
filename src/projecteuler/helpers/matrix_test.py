import unittest
from .matrix import matrix


class TestMatrix(unittest.TestCase):

    def test_matrix_3x3(self):

        side_n = 3
        side_m = 3
        fill = 1

        self.assertEqual(matrix(side_n, side_m, fill), [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ])

    def test_matrix_3x3_none(self):

        side_n = 3
        side_m = 3
        fill = None

        self.assertEqual(matrix(side_n, side_m, fill), [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ])

    def test_matrix_3x5(self):

        side_n = 3
        side_m = 5
        fill = None

        self.assertEqual(matrix(side_n, side_m, fill), [
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None]
        ])

    def test_matrix_5x3(self):

        side_n = 5
        side_m = 3
        fill = None

        self.assertEqual(matrix(side_n, side_m, fill), [
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ])
