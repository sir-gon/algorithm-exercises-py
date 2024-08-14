import unittest
from pathlib import Path

from ....hackerrank.lib.loader import load_test_cases
from .ctci_making_anagrams import make_anagram

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = load_test_cases(FILE_PATH + '/ctci_making_anagrams.testcases.json')


class TestMakeAnagram(unittest.TestCase):

    def test_make_anagram(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                make_anagram(_tt['a'], _tt['b']), _tt['expected'],
                f"{_} | make_anagram({_tt['a']}, {_tt['b']}) must be "
                f"=> {_tt['expected']}")
