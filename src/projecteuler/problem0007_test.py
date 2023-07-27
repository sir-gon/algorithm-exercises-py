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
