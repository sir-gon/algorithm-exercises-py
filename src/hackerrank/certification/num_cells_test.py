import unittest
from .num_cells import num_cells


class TestNumCells(unittest.TestCase):

    def test_get_total_x_case_0(self):

        grid = [
            [1, 2, 7],
            [4, 5, 6],
            [8, 8, 9]
        ]
        solution_found = 2

        self.assertEqual(
            num_cells(grid), solution_found,
            f"get_total_x({grid}) must be "
            f"=> {solution_found}")
