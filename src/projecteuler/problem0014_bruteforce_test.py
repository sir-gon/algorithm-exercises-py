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
