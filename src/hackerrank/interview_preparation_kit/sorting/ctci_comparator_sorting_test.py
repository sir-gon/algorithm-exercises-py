import unittest
from .ctci_comparator_sorting import Player, SortablePlayer, comparator_sorting


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
        },
        {
            'title': 'Sample Test Case 6',
            'input': [
                SortablePlayer('smith', 20),
                SortablePlayer('jones', 15),
                SortablePlayer('jones', 20)
            ],
            'answer': '\n'.join(['jones 20',
                                 'smith 20',
                                 'jones 15'])
        },
        {
            'title': 'Sample Test Case 7',
            'input': [
                SortablePlayer('davis', 15),
                SortablePlayer('davis', 20),
                SortablePlayer('davis', 10),
                SortablePlayer('edgehill', 15)
            ],
            'answer': '\n'.join(['davis 20',
                                 'davis 15',
                                 'edgehill 15',
                                 'davis 10'])
        },
        {
            'title': 'Edge case: draw',
            'input': [
                SortablePlayer('kurt', 100),
                SortablePlayer('kurt', 100)
            ],
            'answer': '\n'.join(['kurt 100',
                                 'kurt 100'])
        },
    ]

    def test_player(self):

        a_player = Player('David', 100)
        a_as_string = str(a_player)
        a_answer = ''

        self.assertEqual(a_as_string, a_answer)

        b_player = Player('Kurt', 10)
        comparator_answer = 0
        self.assertEqual(a_player.comparator(b_player), comparator_answer)

    def test_comparator_sorting(self):

        for _, _tt in enumerate(self.tests):

            self.assertEqual(
                comparator_sorting(_tt['input']), _tt['answer'],
                f"{_} | comparator_sorting({_tt['input']}) must be "
                f"=> {_tt['answer']}")
