import unittest
from .problem0024 import problem0024


class TestProblem0024(unittest.TestCase):

    def test_problem0024_empty_case(self):

        solution_found = ''
        input_elements = ''
        input_permutation_to_find = 6

        self.assertEqual(
            problem0024(input_elements, input_permutation_to_find),
            solution_found,
            f"problem0024({input_elements}, {input_permutation_to_find}) must be "
            f"=> {input_permutation_to_find}")

    def test_problem0024_small_case(self):

        solution_found = 'ADCB'
        input_elements = 'ABCD'
        input_permutation_to_find = 6

        self.assertEqual(
            problem0024(input_elements, input_permutation_to_find),
            solution_found,
            f"problem0024({input_elements}, {input_permutation_to_find}) must be "
            f"=> {input_permutation_to_find}")

    def test_problem0024_full_case(self):

        solution_found = '2783915460'
        input_elements = '0123456789'
        input_permutation_to_find = 1000000

        self.assertEqual(
            problem0024(input_elements, input_permutation_to_find),
            solution_found,
            f"problem0024({input_elements}, {input_permutation_to_find}) must be "
            f"=> {input_permutation_to_find}")
