import unittest
from pathlib import Path

from ....lib.loader import loadTestCases
from .roads_and_libraries import roadsAndLibraries

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = loadTestCases(
    FILE_PATH + '/roads_and_libraries.testcases.json')


class TestRoadsAndLibraries(unittest.TestCase):

    def test_roads_and_libraries(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                roadsAndLibraries(
                    _tt['n'],
                    _tt['c_lib'],
                    _tt['c_road'],
                    _tt['cities']
                ),
                _tt['expected'],
                f"{_} | roads_and_libraries("
                f"{_tt['n']},"
                f"{_tt['c_lib']},"
                f"{_tt['c_road']},"
                f"{_tt['cities']}) must be "
                f"=> {_tt['expected']}")
