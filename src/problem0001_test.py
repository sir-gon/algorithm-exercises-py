###############################################################################
# Multiples of 3 and 5
#
# https://projecteuler.net/problem=1
#
# If we list all the natural numbers below 10 that are multiples
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
###############################################################################

import unittest
from .problem0001 import problem0001

class TestProblem0001(unittest.TestCase):

    def test_problem0001(self):

        _expected_found = 233168
        _input_top = 1000

        self.assertEqual(problem0001(_input_top), _expected_found)
