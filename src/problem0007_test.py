###############################################################################
# 10001st prime
#
# https://projecteuler.net/problem=7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
################################################################################

import os
import unittest
from .problem0007 import problem0007

BRUTEFORCE = os.getenv('BRUTEFORCE')
BRUTEFORCE = BRUTEFORCE.upper() == "TRUE" if BRUTEFORCE is not None else False


class TestProblem0007(unittest.TestCase):

    def test_problem0007(self):

        expected_answer = 13
        top = 6

        self.assertEqual(problem0007(top), expected_answer)
