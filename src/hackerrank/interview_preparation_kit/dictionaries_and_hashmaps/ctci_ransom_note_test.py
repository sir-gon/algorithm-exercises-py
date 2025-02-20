import unittest
from pathlib import Path

from ....hackerrank.lib.loader import load_test_cases
from .ctci_ransom_note import checkMagazine, checkMagazineText

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = load_test_cases(
    FILE_PATH + '/ctci_ransom_note.testcases.json')


class TestCheckMagazine(unittest.TestCase):

    def test_check_magazine(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                checkMagazineText(_tt['magazine'], _tt['note']), _tt['expected'],
                f"{_} | checkMagazineText({_tt['magazine']}, {_tt['note']}) must be "
                f"=> {_tt['expected']}")

            # Print the result (for coverage)
            checkMagazine(_tt['magazine'], _tt['note'])
