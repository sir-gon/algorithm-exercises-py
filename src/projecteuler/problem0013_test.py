import unittest
from .problem0013 import problem0013

from .data.problem0013 import problem0013Data


class TestProblem0013(unittest.TestCase):

    def test_problem0013(self):

        answer = 5537376230
        firts_digits = 10

        self.assertEqual(
            problem0013(problem0013Data, firts_digits), answer,
            f"problem0013({problem0013Data}) must be "
            f"=> {answer}")
