import unittest
from .problem0014 import problem0014


class TestProblem0014(unittest.TestCase):

    def test_problem0014(self):

        epsilon = 10000
        found = 837799

        tests = [
          {'bottom': found - epsilon, 'top': found + epsilon, 'answer': found}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0014(_tt['bottom'], _tt['top']), _tt['answer'],
                f"{_} | problem0014({_tt['bottom'], _tt['top']}) must be "
                f"=> {_tt['answer']}")

    def test_problem0014_border_case_bottom_negative(self):

        tests = [
          {'bottom': -1, 'top': 1}
        ]

        for _, _tt in enumerate(tests):

            self.assertRaisesRegex(ValueError,
                                   'bottom must be a positive integer',
                                   problem0014, _tt['bottom'], _tt['top'])

    def test_problem0014_border_case_bottom_top_invertion(self):

        tests = [
          {'bottom': 10, 'top': 0}
        ]

        for _, _tt in enumerate(tests):

            self.assertRaisesRegex(ValueError,
                                   'top must be and integer, higher than bottom',
                                   problem0014, _tt['bottom'], _tt['top'])
