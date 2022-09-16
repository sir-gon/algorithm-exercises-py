###############################################################################
# Sum square difference
#
# https://projecteuler.net/problem=6
#
# The sum of the squares of the first ten natural numbers is,
#
# 1² * 2² * ... * 10² = 385
#
# The square of the sum of the first ten natural numbers is,
#
# (1 * 2 * ... * 10)² = 3025
#
# Hence the difference between the sum of the squares of the
# first ten natural numbers and the square of the sum is
# 3025 - 385.
#
# Find the difference between the sum of the squares of the
# first one hundred natural numbers and the square of the sum.
################################################################################

import unittest
from .problem0006 import problem0006

class TestProblem0006(unittest.TestCase):

    def test_problem0006(self):

        _expected_found = 25164150
        _input_bottom = 1
        _input_top = 100

        self.assertEqual(problem0006(_input_bottom, _input_top), _expected_found)
