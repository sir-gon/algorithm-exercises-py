import unittest
from .ctci_array_left_rotation import rot_left, rot_left_one


class TestArrayLeftRotation(unittest.TestCase):

    def test_rot_left_one(self):

        tests = [
          {'input': [1, 2, 3, 4, 5], 'answer': [2, 3, 4, 5, 1]},
          {'input': [2, 3, 4, 5, 1], 'answer': [3, 4, 5, 1, 2]},
          {'input': [3, 4, 5, 1, 2], 'answer': [4, 5, 1, 2, 3]},
          {'input': [4, 5, 1, 2, 3], 'answer': [5, 1, 2, 3, 4]},
          {'input': [5, 1, 2, 3, 4], 'answer': [1, 2, 3, 4, 5]},
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                rot_left_one(_tt['input']), _tt['answer'],
                f"{_} | rot_left({_tt['input']}) must be "
                f"=> {_tt['answer']}")

    def test_rot_left(self):

        tests = [
          {'input': [1, 2, 3, 4, 5], 'd': 4, 'answer': [5, 1, 2, 3, 4]},
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                rot_left(_tt['input'], _tt['d']), _tt['answer'],
                f"{_} | rot_left({_tt['input']}) must be "
                f"=> {_tt['answer']}")
