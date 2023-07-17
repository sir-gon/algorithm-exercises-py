###############################################################################
# Longest Collatz sequence
#
# https://projecteuler.net/problem=14
#
#
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all
# starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
################################################################################

import unittest
from .problem0014 import problem0014


class TestProblem0014(unittest.TestCase):

    def test_problem0014(self):

        epsilon = 10000
        found = 837799

        tests = [
          {'bottom': found - epsilon, 'top': found + epsilon, 'answer': found}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0014(_tt['bottom'], _tt['top']), _tt['answer'],
                f"{_} | problem0014({_tt['bottom'], _tt['top']}) must be "
                f"=> {_tt['answer']}")

    def test_problem0014_border_case_bottom_negative(self):

        tests = [
          {'bottom': -1, 'top': 1}
        ]

        for _, _tt in enumerate(tests):

            self.assertRaisesRegex(ValueError,
                                   'bottom must be a positive integer',
                                   problem0014, _tt['bottom'], _tt['top'])

    def test_problem0014_border_case_bottom_top_invertion(self):

        tests = [
          {'bottom': 10, 'top': 0}
        ]

        for _, _tt in enumerate(tests):

            self.assertRaisesRegex(ValueError,
                                   'top must be and integer, higher than bottom',
                                   problem0014, _tt['bottom'], _tt['top'])
