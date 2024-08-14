import unittest
from pathlib import Path

from ....hackerrank.lib.loader import load_test_cases
from .alternating_characters import alternating_characters

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = load_test_cases(FILE_PATH + '/alternating_characters.testcases.json')


class TestAlternatingCharacters(unittest.TestCase):

    def test_alternating_characters(self):

        for _, testset in enumerate(TEST_CASES):

            for _, _tt in enumerate(testset['tests']):

                self.assertEqual(
                    alternating_characters(_tt['input']), _tt['expected'],
                    f"{_} | alternating_characters({_tt['input']}) must be "
                    f"=> {_tt['expected']}")
