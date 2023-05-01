###############################################################################
# Special Pythagorean triplet
#
# https://projecteuler.net/problem=9
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a² + b² = c²
# For example, 3² + 4² = 9 + 16 = 25 = 5².
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
###############################################################################

import unittest
from .problem0009 import problem0009


class TestProblem0009(unittest.TestCase):

    def test_problem0009_basic(self):

        tests = [
          {
            'inputTopLimit': 3 + 4 + 5,
            'answer': 3 * 4 * 5
          },
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0009(_tt['inputTopLimit']), _tt['answer'],
                f"{_} | problem0009({_tt['inputTopLimit']}) must be "
                f"=> {_tt['answer']}")

    def test_problem0009_full(self):

        tests = [
          {
            'inputTopLimit': 200 + 375 + 425,
            'answer': 200 * 375 * 425
          },
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0009(_tt['inputTopLimit']), _tt['answer'],
                f"{_} | problem0009({_tt['inputTopLimit']}) must be "
                f"=> {_tt['answer']}")
