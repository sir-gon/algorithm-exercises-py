###############################################################################
# Amicable numbers
#
# https://projecteuler.net/problem=21
#
# Let d(n) be defined as the sum of proper divisors of n
# (numbers less than n which divide evenly into n).
#
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are
# an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10,
# 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
#
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10021.
#
###############################################################################
# Result found: 31626
# Amicable numbers found:
# amicableNumbers [
#      '220',  '284',
#      '1184', '1210',
#      '2620', '2924',
#      '5020', '5564',
#      '6232', '6368'
#    ]
###############################################################################

import unittest
from .problem0021 import problem0021


class TestProblem0021(unittest.TestCase):

    def test_problem0021(self):

        tests = [
          {'inputStart': 1, 'inputLimit': 10000, 'answer': 31626}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0021(_tt['inputStart'], _tt['inputLimit']), _tt['answer'],
                f"{_} | problem0021({_tt['inputStart']}, {_tt['inputLimit']}) must be "
                f"=> {_tt['answer']}")
