import unittest
from pathlib import Path

from ....lib.loader import loadTestCases
from .ctci_ransom_note import checkMagazine, checkMagazineText

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = loadTestCases(
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
