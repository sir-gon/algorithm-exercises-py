import unittest
from .solve_me_first import solve_me_first


class TestSolveMeFirst(unittest.TestCase):

    def test_solve_me_first(self):

        tests = [
            {'a': 0, 'b': 0, 'answer': 0}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                solve_me_first(_tt['a'], _tt['b']), _tt['answer'],
                f"{_} | solve_me_first({_tt['a'], _tt['b']}) must be "
                f"=> {_tt['answer']}")
