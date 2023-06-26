###############################################################################
# Counting Sundays

# https://projecteuler.net/problem=19

# You are given the following information, but you may prefer
# to do some research for yourself.

#  1 Jan 1900 was a Monday.
#  Thirty days has September,
#    April, June and November.
#    All the accumulatedRemainder have thirty-one,
#    Saving February alone,
#    Which has twenty-eight, rain or shine.
#    And on leap years, twenty-nine.
#  A leap year occurs on any year evenly divisible by 4,
#    but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the
# twentieth century (1 Jan 1901 to 31 Dec 2000)?
################################################################################

import unittest
from .problem0019 import problem0019
from .constants.datetime import __SUNDAY__


class TestProblem0019(unittest.TestCase):

    def test_problem0019_small(self):

        since_input = 1900
        until_input = 1901
        solution_found = 2

        self.assertEqual(
            problem0019(__SUNDAY__, since_input, until_input),
            solution_found,
            f"problem0019({since_input}, {until_input}) must be "
            f"=> {solution_found}")

    def test_problem0019_full(self):

        since_input = 1901
        until_input = 2000
        solution_found = 171

        self.assertEqual(
            problem0019(__SUNDAY__, since_input, until_input),
            solution_found,
            f"problem0019({since_input}, {until_input}) must be "
            f"=> {solution_found}")
