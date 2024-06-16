import unittest
from .problem0003 import problem0003


class TestProblem0003(unittest.TestCase):

    def test_problem0003(self):

        tests = [
            {'input': 600851475143, 'answer': 6857}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0003(_tt['input']), _tt['answer'],
                f"{_} | problem0003({_tt['input']}) must be "
                f"=> {_tt['answer']}")

    def test_problem0003_small_cases(self):

        tests = [
            {'input': 6, 'answer': 3},
            {'input': 10, 'answer': 5},
            {'input': 17, 'answer': 17}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0003(_tt['input']), _tt['answer'],
                f"{_} | problem0003({_tt['input']}) must be "
                f"=> {_tt['answer']}")

    def test_problem0003_basic(self):

        tests = [
            {'input': 13195, 'answer': 29}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0003(_tt['input']), _tt['answer'],
                f"{_} | problem0003({_tt['input']}) must be "
                f"=> {_tt['answer']}")

    def test_problem0003_odd_divisors(self):

        tests = [
            {'input': 16, 'answer': 2}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0003(_tt['input']), _tt['answer'],
                f"{_} | problem0003({_tt['input']}) must be "
                f"=> {_tt['answer']}")
