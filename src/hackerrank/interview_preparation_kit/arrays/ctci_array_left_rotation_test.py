import unittest
from .ctci_array_left_rotation import rot_left


class TestArrayLeftRotation(unittest.TestCase):

    def test_ctci_array_left_rotation(self):

        tests = [
          {'input': [1, 2, 3, 4, 5], 'answer': [1, 2, 3, 4, 5]},
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                rot_left(_tt['input']), _tt['answer'],
                f"{_} | rot_left({_tt['input']}) must be "
                f"=> {_tt['answer']}")
