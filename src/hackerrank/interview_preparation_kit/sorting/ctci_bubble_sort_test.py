import unittest
from pathlib import Path

from ....hackerrank.lib.loader import load_test_cases
from .ctci_bubble_sort import SortableGroup, count_swaps

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = load_test_cases(FILE_PATH + '/ctci_bubble_sort.testcases.json')


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
                count_swaps(_tt['input']), expected,
                f"{_} | count_swaps({_tt['input']}) must be "
                f"=> {expected}")
