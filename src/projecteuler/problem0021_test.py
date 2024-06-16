import unittest
from .problem0021 import problem0021


class TestProblem0021(unittest.TestCase):

    def test_problem0021(self):

        tests = [
            {'inputStart': 1, 'inputLimit': 10000, 'answer': 31626}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0021(_tt['inputStart'], _tt['inputLimit']), _tt['answer'],
                f"{_} | problem0021({_tt['inputStart']}, {_tt['inputLimit']}) must be "
                f"=> {_tt['answer']}")
