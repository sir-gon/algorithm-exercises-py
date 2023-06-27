###############################################################################
# Lexicographic Permutations
#
# https://projecteuler.net/problem=24
#
# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically,
# we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the
# digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
################################################################################

import unittest
from .problem0024 import problem0024


class TestProblem0024(unittest.TestCase):

    def test_problem0024_empty_case(self):

        solution_found = []
        input_elements = []
        input_permutation_to_find = 6

        self.assertEqual(
            problem0024(input_elements, input_permutation_to_find),
            solution_found,
            f"problem0024({input_elements}, {input_permutation_to_find}) must be "
            f"=> {input_permutation_to_find}")

    def test_problem0024_small_case(self):

        solution_found = ['A', 'D', 'C', 'B']
        input_elements = list('ABCD')
        input_permutation_to_find = 6

        self.assertEqual(
            problem0024(input_elements, input_permutation_to_find),
            solution_found,
            f"problem0024({input_elements}, {input_permutation_to_find}) must be "
            f"=> {input_permutation_to_find}")

    def test_problem0024_full_case(self):

        solution_found = ['2', '7', '8', '3', '9', '1', '5', '4', '6', '0']
        input_elements = list('0123456789')
        input_permutation_to_find = 1000000

        self.assertEqual(
            problem0024(input_elements, input_permutation_to_find),
            solution_found,
            f"problem0024({input_elements}, {input_permutation_to_find}) must be "
            f"=> {input_permutation_to_find}")
