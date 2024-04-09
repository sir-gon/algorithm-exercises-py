import unittest
from .ctci_comparator_sorting import SortablePlayer, comparator_sorting


class TestComparatorSorting(unittest.TestCase):
    tests = [
        {
            'title': 'Sample Test Case 0',
            'input': [
                    SortablePlayer('amy', 100),
                    SortablePlayer('david', 100),
                    SortablePlayer('heraldo', 50),
                    SortablePlayer('aakansha', 75),
                    SortablePlayer('aleksa', 150)
                ],
            'answer': '\n'.join(['aleksa 150',
                                 'amy 100',
                                 'david 100',
                                 'aakansha 75',
                                 'heraldo 50'])
        }
    ]

    def test_comparator_sorting(self):

        for _, _tt in enumerate(self.tests):

            self.assertEqual(
                comparator_sorting(_tt['input']), _tt['answer'],
                f"{_} | comparator_sorting({_tt['input']}) must be "
                f"=> {_tt['answer']}")
