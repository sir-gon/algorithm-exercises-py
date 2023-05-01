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

    def test_problem0006_basic(self):

        tests = [
          {'input_bottom': 1, 'input_top': 10, 'answer': 3025 - 385}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0006(_tt['input_bottom'], _tt['input_top']),
                _tt['answer'],
                f"{_} | problem0006({_tt['input_bottom']}, {_tt['input_top']})"
                f" must be => {_tt['answer']}")

    def test_problem0006_full(self):

        tests = [
          {'input_bottom': 1, 'input_top': 100, 'answer': 25164150}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0006(_tt['input_bottom'], _tt['input_top']),
                _tt['answer'],
                f"{_} | problem0006({_tt['input_bottom']}, {_tt['input_top']})"
                f" must be => {_tt['answer']}")
