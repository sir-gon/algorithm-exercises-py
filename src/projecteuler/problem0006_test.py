import unittest
from .problem0006 import problem0006


class TestProblem0006(unittest.TestCase):

    def test_problem0006_basic(self):

        tests = [
            {'input_bottom': 1, 'input_top': 10, 'answer': 3025 - 385}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0006(_tt['input_bottom'], _tt['input_top']),
                _tt['answer'],
                f"{_} | problem0006({_tt['input_bottom']}, {_tt['input_top']})"
                f" must be => {_tt['answer']}")

    def test_problem0006_full(self):

        tests = [
            {'input_bottom': 1, 'input_top': 100, 'answer': 25164150}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0006(_tt['input_bottom'], _tt['input_top']),
                _tt['answer'],
                f"{_} | problem0006({_tt['input_bottom']}, {_tt['input_top']})"
                f" must be => {_tt['answer']}")
