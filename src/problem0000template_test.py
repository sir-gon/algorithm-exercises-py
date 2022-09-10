###############################################################################
# <TITLE>
#
# https://projecteuler.net/problem=XX
#
# <DESCRIPTION>
#
################################################################################

import unittest
from .problem0000template import problem0000

class TestProblem0000(unittest.TestCase):

    def test_problem0000(self):

        _expected_found = 0

        self.assertEqual(problem0000(), _expected_found)
