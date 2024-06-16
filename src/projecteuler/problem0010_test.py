import unittest
from .problem0010 import problem0010


class TestProblem0010(unittest.TestCase):

    def test_problem0010_basic(self):

        tests = [
            {'inputLimit': 10, 'answer': 17}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0010(_tt['inputLimit']), _tt['answer'],
                f"{_} | problem0010({_tt['inputLimit']}) must be "
                f"=> {_tt['answer']}")
