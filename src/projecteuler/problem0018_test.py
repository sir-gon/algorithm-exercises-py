import unittest
from .problem0018 import problem0018
from .data.problem0018 import problem0018Data

small_case = [
    [3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3]
]


class TestProblem0018(unittest.TestCase):

    def test_problem0018_small_case(self):

        tests = [
          {'input': small_case, 'answer': 23}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0018(_tt['input']), _tt['answer'],
                f"{_} | problem0018({_tt['input']}) must be "
                f"=> {_tt['answer']}")

    def test_problem0018(self):

        tests = [
          {'input': problem0018Data, 'answer': 1074}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0018(_tt['input']), _tt['answer'],
                f"{_} | problem0018({_tt['input']}) must be "
                f"=> {_tt['answer']}")
