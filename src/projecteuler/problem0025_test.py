import unittest
from .problem0025 import problem0025


class TestProblem0025(unittest.TestCase):

    def test_problem0025(self):

        tests = [
            {'input': 3, 'answer': 12}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0025(_tt['input']), _tt['answer'],
                f"{_} | problem0025({_tt['input']}) must be "
                f"=> {_tt['answer']}")

    def test_problem0025_full(self):

        tests = [
            {'input': 1000, 'answer': 4782}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0025(_tt['input']), _tt['answer'],
                f"{_} | problem0025({_tt['input']}) must be "
                f"=> {_tt['answer']}")
