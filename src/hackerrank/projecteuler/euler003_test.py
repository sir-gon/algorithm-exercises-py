import unittest
from .euler003 import euler003


class TestEuler003(unittest.TestCase):

    def test_euler003(self):

        tests = [
            {'n': 1, 'answer': None},
            {'n': 10, 'answer': 5},
            {'n': 17, 'answer': 17}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                euler003(_tt['n']), _tt['answer'],
                f"{_} | euler003({_tt['n']}) must be "
                f"=> {_tt['answer']}")
