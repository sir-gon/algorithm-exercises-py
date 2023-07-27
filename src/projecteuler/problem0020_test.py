import unittest
from .problem0020 import problem0020


class TestProblem0020(unittest.TestCase):

    def test_problem0020_small(self):

        input_factorial = 10
        solution_found = 27

        self.assertEqual(
            problem0020(input_factorial),
            solution_found,
            f"problem0020({input_factorial}) must be "
            f"=> {solution_found}")

    def test_problem0020_full(self):

        input_factorial = 100
        solution_found = 648

        self.assertEqual(
            problem0020(input_factorial),
            solution_found,
            f"problem0020({input_factorial}) must be "
            f"=> {solution_found}")
