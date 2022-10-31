###############################################################################
# Summation of primes
#
# https:##projecteuler.net/problem=10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
###############################################################################

## ############################################################################
## About solution: BRUTE FORCE
##
## Found:
## ...
## Prime found 1999969 put in position: 148931
## Prime found 1999979 put in position: 148932
## Prime found 1999993 put in position: 148933
## Sum of primes below 2000000 is: 142913828922
##
## ############################################################################

import unittest
from .problem0010 import problem0010

class TestProblem0010(unittest.TestCase):

    def test_problem0010_basic(self):

        tests = [
          {'inputLimit': 10, 'answer': 17}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual( problem0010(_tt['inputLimit']), _tt['answer'],
              f"{_} | problem0010({_tt['inputLimit']}) must be "\
              f"=> {_tt['answer']}")
