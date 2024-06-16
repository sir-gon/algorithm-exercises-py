import unittest
from .problem0016 import problem0016


class TestProblem0016(unittest.TestCase):

    def test_problem0016_small_case(self):

        tests = [
            {'input_base': 2, 'input_exponent': 15, 'answer': 26}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0016(_tt['input_base'], _tt['input_exponent']), _tt['answer'],
                f"{_} | problem0016({_tt['input_base']}, {_tt['input_exponent']}) "
                f" must be => {_tt['answer']}")

    def test_problem0016_big_case(self):

        tests = [
            {'input_base': 2, 'input_exponent': 1000, 'answer': 1366}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0016(_tt['input_base'], _tt['input_exponent']), _tt['answer'],
                f"{_} | problem0016({_tt['input_base']}, {_tt['input_exponent']}) "
                f" must be => {_tt['answer']}")
