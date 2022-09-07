###############################################################################
# Largest palindrome product
#
# https://projecteuler.net/problem=4
#
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit
# numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
###############################################################################

import unittest
from .problem0004 import problem0004

class TestProblem0004(unittest.TestCase):

    def test_problem0004(self):

        _solution_found = 906609
        _input_bottom = 111
        _input_top = 999

        self.assertEqual(
          problem0004(
            _input_bottom,
            _input_top),
          _solution_found)
