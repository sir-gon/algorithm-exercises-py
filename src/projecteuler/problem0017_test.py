import unittest
from .problem0017 import problem0017


class TestProblem0017(unittest.TestCase):

    def test_problem0017(self):

        tests = [
          {'input_init': 1, 'input_last': 1000, 'answer': 21124}
        ]
        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0017(_tt['input_init'], _tt['input_last']), _tt['answer'],
                f"{_} | problem0017(_tt['input_init'], _tt['input_last']) must be "
                f"=> {_tt['answer']}")
