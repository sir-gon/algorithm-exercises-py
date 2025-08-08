import unittest
from pathlib import Path

from ....lib.loader import loadTestCases
from .ctci_big_o import primality


FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = loadTestCases(
    FILE_PATH + '/ctci_big_o.testcases.json')


class TestCtciBigO(unittest.TestCase):

    def test_ctci_big_o(self):

        for _, testset in enumerate(TEST_CASES):

            for _, _tt in enumerate(testset['tests']):

                self.assertEqual(
                    primality(_tt['input']), _tt['answer'],
                    f"{_} | primality({_tt['input']}) must be "
                    f"=> {_tt['answer']}")

    def test_ctci_big_o_edge_cases(self):
        self.assertEqual(primality(1), "Not prime")
