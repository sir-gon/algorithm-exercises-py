import unittest
from .problem0015 import problem0015


class TestProblem0015(unittest.TestCase):

    def test_problem0015_small(self):

        tests = [
          {'input': 2, 'answer': 6}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0015(_tt['input']), _tt['answer'],
                f"{_} | problem0015({_tt['input']}) must be "
                f"=> {_tt['answer']}")

    def test_problem0015(self):

        tests = [
          {'input': 20, 'answer': 137846528820}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0015(_tt['input']), _tt['answer'],
                f"{_} | problem0015({_tt['input']}) must be "
                f"=> {_tt['answer']}")
