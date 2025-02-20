import unittest
from pathlib import Path

from ....lib.loader import loadTestCases
from .ctci_making_anagrams import makeAnagram

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = loadTestCases(FILE_PATH + '/ctci_making_anagrams.testcases.json')


class TestMakeAnagram(unittest.TestCase):

    def test_make_anagram(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                makeAnagram(_tt['a'], _tt['b']), _tt['expected'],
                f"{_} | makeAnagram({_tt['a']}, {_tt['b']}) must be "
                f"=> {_tt['expected']}")
