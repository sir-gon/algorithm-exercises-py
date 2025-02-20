import unittest
from pathlib import Path

from ....lib.loader import loadTestCases
from .ctci_ice_cream_parlor import whatFlavors


FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = loadTestCases(FILE_PATH + '/ctci_ice_cream_parlor.testcases.json')
TEST_CASES_BORDER_CASES = loadTestCases(
    FILE_PATH + '/ctci_ice_cream_parlor.border_testcases.json')


class TestIceCreamParlor(unittest.TestCase):

    def test_what_flavors(self):

        for _, testset in enumerate(TEST_CASES):

            for _, _tt in enumerate(testset['tests']):

                self.assertEqual(
                    whatFlavors(_tt['costs'], _tt['money']), _tt['expected'],
                    f"{_} | whatFlavors({_tt['costs']}, {_tt['money']}) must be "
                    f"=> {_tt['expected']}")

    def test_what_flavors_border_case(self):

        for _, testset in enumerate(TEST_CASES_BORDER_CASES):

            for _, _tt in enumerate(testset['tests']):

                self.assertEqual(
                    whatFlavors(_tt['costs'], _tt['money']), _tt['expected'],
                    f"{_} | whatFlavors({_tt['costs']}, {_tt['money']}) must be "
                    f"=> {_tt['expected']}")
