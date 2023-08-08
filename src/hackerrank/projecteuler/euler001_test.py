import unittest
from .euler001 import euler001


class TestEuler001(unittest.TestCase):

    def test_euler001(self):

        tests = [
          {'a': 3, 'b': 5, 'n': 10, 'answer': 23},
          {'a': 3, 'b': 5, 'n': 100, 'answer': 2318},
          {'a': 3, 'b': 5, 'n': 1000, 'answer': 233168}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                euler001(_tt['a'], _tt['b'], _tt['n']), _tt['answer'],
                f"{_} | euler001({_tt['a']}, {_tt['b']}, {_tt['n']}) must be "
                f"=> {_tt['answer']}")
