import unittest
import pytest
from .problem0011 import problem0011
from .data.problem0011 import problem0011Data
from .data.problem0011 import problem0011WrongData


class TestProblem0011(unittest.TestCase):

    def test_problem0011(self):

        answer = 70600674
        input_interval = 4

        self.assertEqual(
            problem0011(problem0011Data, input_interval),
            answer,
            f"problem0011({problem0011Data}) must be => {answer}")

    def test_problem0011_wrong_data(self):

        input_interval = 0

        with pytest.raises(Exception):
            problem0011(problem0011WrongData, input_interval)
