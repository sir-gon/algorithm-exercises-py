import unittest
from .ctci_bubble_sort import SortableGroup, count_swaps

NL = "\n"
NUM_SWAPS = '#numSwaps#'
FIRST_ELEMENT = '#firstElement#'
LAST_ELEMENT = '#lastElement#'
ANSWER_TEMPLATE = f'Array is sorted in {NUM_SWAPS} swaps.{NL}' + \
                  f'First Element: {FIRST_ELEMENT}{NL}' + \
                  f'Last Element: {LAST_ELEMENT}{NL}'


class TestBubleSort(unittest.TestCase):

    def test_sorts(self):

        tests = [
            {'input': SortableGroup([6, 4, 1]), 'answer': [1, 4, 6]},
            {'input': SortableGroup([3, 2, 1]), 'answer': [1, 2, 3]},
            {'input': SortableGroup([1, 2, 3]), 'answer': [1, 2, 3]}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                _tt['input'].bubble_sort().group, _tt['answer'],
                f"{_} | count_swaps({_tt['input']}) must be "
                f"=> {_tt['answer']}")

    def test_counts(self):

        tests = [
            {
                'input': [6, 4, 1],
                'answer':
                    ANSWER_TEMPLATE[:]
                    .replace(NUM_SWAPS, '3')
                    .replace(FIRST_ELEMENT, '1')
                    .replace(LAST_ELEMENT, '6')
            },
            {
                'input': [3, 2, 1],
                'answer':
                    ANSWER_TEMPLATE[:]
                    .replace(NUM_SWAPS, '3')
                    .replace(FIRST_ELEMENT, '1')
                    .replace(LAST_ELEMENT, '3')
            },
            {
                'input': [1, 2, 3],
                'answer':
                    ANSWER_TEMPLATE[:]
                    .replace(NUM_SWAPS, '0')
                    .replace(FIRST_ELEMENT, '1')
                    .replace(LAST_ELEMENT, '3')
            },
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                count_swaps(_tt['input']), _tt['answer'],
                f"{_} | count_swaps({_tt['input']}) must be "
                f"=> {_tt['answer']}")
