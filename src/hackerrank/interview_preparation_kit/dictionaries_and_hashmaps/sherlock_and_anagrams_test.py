import unittest
from pathlib import Path

from ....lib.loader import loadTestCases
from .sherlock_and_anagrams import sherlockAndAnagrams

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = loadTestCases(
    FILE_PATH + '/sherlock_and_anagrams.testcases.json')


class TestSherlockAndAnagrams(unittest.TestCase):

    def test_sherlock_and_anagrams(self):

        for _, testset in enumerate(TEST_CASES):

            for _, _tt in enumerate(testset['tests']):

                self.assertEqual(
                    sherlockAndAnagrams(_tt['input']), _tt['expected'],
                    f"{_} | sherlock_and_anagrams({_tt['input']}) must be "
                    f"=> {_tt['expected']}")
