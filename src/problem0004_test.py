###############################################################################
# Largest palindrome product
#
# https://projecteuler.net/problem=4
#
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit
# numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
###############################################################################

import unittest
from .problem0004 import problem0004

class TestProblem0004(unittest.TestCase):

    def test_problem0004(self):

        tests = [
          {'input_bottom': 111, 'input_top': 999, 'answer': 906609}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual( problem0004(_tt['input_bottom'], _tt['input_top']), _tt['answer'],
              f"{_} | problem0004({_tt['input_bottom']}, {_tt['input_top']}) must be "\
              f"=> {_tt['answer']}")
