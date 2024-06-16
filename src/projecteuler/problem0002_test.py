import unittest
from .problem0002 import problem0002


class TestProblem0002(unittest.TestCase):

    def test_problem0002(self):

        tests = [
            {'input': 4000000, 'answer': 4613732}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0002(_tt['input']), _tt['answer'],
                f"{_} | problem0002({_tt['input']}) must be "
                f"=> {_tt['answer']}")
