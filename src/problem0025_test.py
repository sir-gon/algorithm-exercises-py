###############################################################################
# 1000-digit Fibonacci Number
#
# https://projecteuler.net/problem=25
#
# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1
#
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
#
# The 12th term, F12 is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci
# sequence to contain 1000 digits?
################################################################################

import unittest
from .problem0025 import problem0025


class TestProblem0025(unittest.TestCase):

    def test_problem0025(self):

        tests = [
          {'input': 3, 'answer': 12}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0025(_tt['input']), _tt['answer'],
                f"{_} | problem0025({_tt['input']}) must be "
                f"=> {_tt['answer']}")

    def test_problem0025_full(self):

        tests = [
          {'input': 1000, 'answer': 4782}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0025(_tt['input']), _tt['answer'],
                f"{_} | problem0025({_tt['input']}) must be "
                f"=> {_tt['answer']}")
