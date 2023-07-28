import os
import unittest
from .problem0007 import problem0007

BRUTEFORCE = os.getenv('BRUTEFORCE')
BRUTEFORCE = BRUTEFORCE.upper() == "TRUE" if BRUTEFORCE is not None else False


class TestProblem0007BruteForce(unittest.TestCase):

    @unittest.skipIf(not BRUTEFORCE, "skipping due a is a large BRUTEFORCE test")
    def test_problem0007_full(self):

        expected_answer = 104743
        top = 10001

        self.assertEqual(problem0007(top), expected_answer)
