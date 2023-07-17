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

        tests = [
          {'input_bottom': 1, 'input_top': 10, 'start_from': 1, 'answer': 2520}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0005(_tt['input_bottom'], _tt['input_top'], _tt['start_from']),
                _tt['answer'],
                f"{_} | problem0005({_tt['input_bottom']}, {_tt['input_top']})"
                f" must be => {_tt['answer']}")

    def test_problem0005_alt_basic(self):

        tests = [
          {'input_bottom': 1, 'input_top': 10, 'answer': 2520}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0005_alt(_tt['input_bottom'], _tt['input_top']),
                _tt['answer'],
                f"{_} | problem0005_alt({_tt['input_bottom']}, {_tt['input_top']})"
                f" must be => {_tt['answer']}")

    def test_problem0005_alt_full(self):

        tests = [
          {'input_bottom': 1, 'input_top': 20, 'answer': 232792560}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0005_alt(_tt['input_bottom'], _tt['input_top']),
                _tt['answer'],
                f"{_} | problem0005_alt({_tt['input_bottom']}, {_tt['input_top']})"
                f" must be => {_tt['answer']}")
