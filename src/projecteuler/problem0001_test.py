import unittest
from .problem0001 import problem0001


class TestProblem0001(unittest.TestCase):

    def test_problem0001_basic(self):

        tests = [
          {'input': 10, 'answer': 23}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0001(_tt['input']), _tt['answer'],
                f"{_} | problem0001({_tt['input']}) must be "
                f"=> {_tt['answer']}")

    def test_problem0001_full(self):

        tests = [
          {'input': 1000, 'answer': 233168}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0001(_tt['input']), _tt['answer'],
                f"{_} | problem0001({_tt['input']}) must be "
                f"=> {_tt['answer']}")
