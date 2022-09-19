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

    def test_problem0001_basic(self):

        tests = [
          {'input': 10, 'answer': 23}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual( problem0001(_tt['input']), _tt['answer'],
              f"{_} | problem0001({_tt['input']}) must be "\
              f"=> {_tt['answer']}")

    def test_problem0001_full(self):

        tests = [
          {'input': 1000, 'answer': 233168}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual( problem0001(_tt['input']), _tt['answer'],
              f"{_} | problem0001({_tt['input']}) must be "\
              f"=> {_tt['answer']}")
