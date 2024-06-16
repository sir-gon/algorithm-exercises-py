import unittest
from .euler002 import euler002


class TestEuler002(unittest.TestCase):

    def test_euler002(self):

        tests = [
            {'n': 10, 'answer': 10},
            {'n': 100, 'answer': 44}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                euler002(_tt['n']), _tt['answer'],
                f"{_} | euler002({_tt['n']}) must be "
                f"=> {_tt['answer']}")
