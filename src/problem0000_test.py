import unittest
from .problem0000 import problem0000


class TestProblem0000(unittest.TestCase):

    def test_problem0000(self):

        tests = [
            {'input': 0, 'answer': 0}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0000(_tt['input']), _tt['answer'],
                f"{_} | problem0000({_tt['input']}) must be "
                f"=> {_tt['answer']}")
