import unittest
import json
from pathlib import Path

from .sherlock_and_anagrams import sherlock_and_anagrams

FILE_PATH = str(Path(__file__).resolve().parent)
JSON_DATA_FILE = FILE_PATH + '/sherlock_and_anagrams.json'
with open(JSON_DATA_FILE, encoding="utf-8") as file:
    TEST_CASES = json.load(file)


class TestSherlockAndAnagrams(unittest.TestCase):

    def test_sherlock_and_anagrams(self):

        for _, testset in enumerate(TEST_CASES):

            for _, _tt in enumerate(testset['tests']):

                self.assertEqual(
                    sherlock_and_anagrams(_tt['input']), _tt['expected'],
                    f"{_} | sherlock_and_anagrams({_tt['input']}) must be "
                    f"=> {_tt['expected']}")
