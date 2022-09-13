###############################################################################
# Smallest multiple
#
# https://projecteuler.net/problem=5
#
# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by
# all of the numbers from 1 to 20?
###############################################################################

import unittest
from .problem0005 import problem0005
from .problem0005_alt import problem0005_alt

class TestProblem0005(unittest.TestCase):

    def test_problem0005_basic(self):

        solution_found = 2520
        bottom = 1
        top = 10
        start_from = 1

        self.assertEqual(problem0005(bottom, top, start_from), solution_found)

    def test_problem0005_full(self):

        solution_found = 232792560
        bottom = 1
        top = 20
        start_from = solution_found - 1000

        self.assertEqual(problem0005(bottom, top, start_from), solution_found)

    def test_problem0005_alt_basic(self):

        solution_found = 2520
        bottom = 1
        top = 10

        self.assertEqual(problem0005_alt(bottom, top), solution_found)

    def test_problem0005_alt_full(self):

        solution_found = 232792560
        bottom = 1
        top = 20

        self.assertEqual(problem0005_alt(bottom, top), solution_found)
