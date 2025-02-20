import unittest
from pathlib import Path

from ..lib.loader import loadTestCases
from .problem0022 import problem0022


FILE_PATH = str(Path(__file__).resolve().parent)

NAMES = loadTestCases(
    FILE_PATH + '/data/p022_names.json')


class TestProblem0022(unittest.TestCase):

    def test_problem0022(self):

        solution_found = 871198282

        self.assertEqual(
            problem0022(NAMES), solution_found,
            f"problem0022({NAMES}) must be "
            f"=> {solution_found}")
