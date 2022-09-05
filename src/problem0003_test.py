###############################################################################
# Largest prime factor
#
# https://projecteuler.net/problem=3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
###############################################################################

import unittest
from .problem0003 import problem0003

class TestProblem0003(unittest.TestCase):

    def test_problem0003(self):

        _expected_found = 6857
        _top = 600851475143

        self.assertEqual(problem0003(_top), _expected_found)

    def test_problem0003_basic(self):

        _expected_found = 29
        _input_top = 13195

        self.assertEqual(problem0003(_input_top), _expected_found)

    def test_problem0003_odd_divisors(self):

        _expected_found = 2
        _input_top = 16

        self.assertEqual(problem0003(_input_top), _expected_found)
