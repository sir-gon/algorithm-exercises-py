###############################################################################
# Longest Collatz sequence
#
# https://projecteuler.net/problem=14
#
#
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all
# starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
################################################################################

import os
import unittest
from .problem0014 import problem0014

BRUTEFORCE = os.getenv('BRUTEFORCE')
BRUTEFORCE = BRUTEFORCE.upper() == "TRUE" if BRUTEFORCE is not None else False


class TestProblem0014(unittest.TestCase):

    @unittest.skipIf(not BRUTEFORCE, "skipping due a is a large BRUTEFORCE test")
    def test_problem0014_brute_force(self):

        bottom = 1
        top = 1000000
        answer = 837799

        self.assertEqual(
            problem0014(bottom, top), answer,
            f"problem0014({bottom, top}) must be => {answer}"
        )
