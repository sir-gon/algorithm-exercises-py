import unittest
from .problem0023 import problem0023


class TestProblem0023(unittest.TestCase):

    def test_problem002_small_case(self):

        solution_found = 276
        input_under_limit = 12
        input_super_limit = 24

        self.assertEqual(
            problem0023(input_under_limit, input_super_limit),
            solution_found,
            f"problem0023({input_under_limit}, {input_super_limit}) must be "
            f"=> {solution_found}")

    def test_problem0023_full_case(self):

        solution_found = 4179871
        input_under_limit = 12
        input_super_limit = 28123

        self.assertEqual(
            problem0023(input_under_limit, input_super_limit),
            solution_found,
            f"problem0023({input_under_limit}, {input_super_limit}) must be "
            f"=> {solution_found}")
