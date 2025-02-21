import unittest
from pathlib import Path

from ....lib.loader import loadTestCases
from .ctci_array_left_rotation import rotLeft

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = loadTestCases(
    FILE_PATH + '/ctci_array_left_rotation.testcases.json')


class TestArrayLeftRotation(unittest.TestCase):

    def test_rot_left(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                rotLeft(_tt['input'], _tt['d_rotations']), _tt['expected'],
                f"{_} | rotLeft({_tt['input'], _tt['d_rotations']}) must be "
                f"=> {_tt['expected']}")
