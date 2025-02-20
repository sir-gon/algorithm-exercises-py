import unittest
from pathlib import Path

from ....lib.loader import loadTestCases
from .ctci_bubble_sort import SortableGroup, countSwaps

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = loadTestCases(FILE_PATH + '/ctci_bubble_sort.testcases.json')


class TestBubleSort(unittest.TestCase):

    def test_sorts(self):

        for _, _tt in enumerate(TEST_CASES):

            to_test = SortableGroup(_tt['input'])

            self.assertEqual(
                to_test.bubble_sort().group, _tt['sorted'],
                f"{_} | SortableGroup({_tt['input']}).bubble_sort().group must be "
                f"=> {_tt['sorted']}")

    def test_counts(self):

        for _, _tt in enumerate(TEST_CASES):

            expected: str = _tt['expected'].replace('\n', "\n")

            self.assertEqual(
                countSwaps(_tt['input']), expected,
                f"{_} | countSwaps({_tt['input']}) must be "
                f"=> {expected}")
