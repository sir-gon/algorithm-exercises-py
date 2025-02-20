import unittest
from pathlib import Path

from ....lib.loader import loadTestCases
from .alternating_characters import alternatingCharacters

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = loadTestCases(FILE_PATH + '/alternating_characters.testcases.json')


class TestAlternatingCharacters(unittest.TestCase):

    def test_alternating_characters(self):

        for _, testset in enumerate(TEST_CASES):

            for _, _tt in enumerate(testset['tests']):

                self.assertEqual(
                    alternatingCharacters(_tt['input']), _tt['expected'],
                    f"{_} | alternatingCharacters({_tt['input']}) must be "
                    f"=> {_tt['expected']}")
