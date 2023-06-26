###############################################################################
# <TITLE>
#
# https://projecteuler.net/problem=XX
#
# <DESCRIPTION>
#
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
