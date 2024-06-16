import unittest
from .problem0012 import problem0012


class TestProblem0012(unittest.TestCase):

    def test_problem0012_basic(self):

        tests = [
            {'input': 5, 'answer': 28}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0012(_tt['input']),
                _tt['answer'],
                f"{_} | problem0012({_tt['input']}) must be => {_tt['answer']}")
