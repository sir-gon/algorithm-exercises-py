import unittest
from .new_year_chaos import minimum_bribes


class TestArrayLeftRotation(unittest.TestCase):

    def test_minimum_bribes(self):

        tests = [
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                minimum_bribes(_tt['input']), _tt['answer'],
                f"{_} | rot_left({_tt['input']}) must be "
                f"=> {_tt['answer']}")
