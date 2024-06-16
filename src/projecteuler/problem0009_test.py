import unittest
from .problem0009 import problem0009


class TestProblem0009(unittest.TestCase):

    def test_problem0009_basic(self):

        tests = [
            {
                'inputTopLimit': 3 + 4 + 5,
                'answer': 3 * 4 * 5
            },
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0009(_tt['inputTopLimit']), _tt['answer'],
                f"{_} | problem0009({_tt['inputTopLimit']}) must be "
                f"=> {_tt['answer']}")

    def test_problem0009_full(self):

        tests = [
            {
                'inputTopLimit': 200 + 375 + 425,
                'answer': 200 * 375 * 425
            },
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0009(_tt['inputTopLimit']), _tt['answer'],
                f"{_} | problem0009({_tt['inputTopLimit']}) must be "
                f"=> {_tt['answer']}")

    def test_problem0009_border_case(self):

        tests = [
            {
                'inputTopLimit': 1 + 2 + 3,
                'answer': None
            },
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0009(_tt['inputTopLimit']), _tt['answer'],
                f"{_} | problem0009({_tt['inputTopLimit']}) must be "
                f"=> {_tt['answer']}")
