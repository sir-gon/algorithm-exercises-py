#!/usr/bin/env python3

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
from .problem0000template import problem0000

class TestProblem0000(unittest.TestCase):

    def test_problem0000(self):

        _expected_found = 0

        self.assertEqual(problem0000(), _expected_found)
