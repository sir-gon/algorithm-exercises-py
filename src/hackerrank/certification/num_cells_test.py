import unittest
from .num_cells import num_cells


class TestNumCells(unittest.TestCase):

    def test_num_cells_case_0(self):

        grid = [
            [1, 2, 7],
            [4, 5, 6],
            [8, 8, 9]
        ]
        solution_found = 2

        self.assertEqual(
            num_cells(grid), solution_found,
            f"num_cells({grid}) must be "
            f"=> {solution_found}")
