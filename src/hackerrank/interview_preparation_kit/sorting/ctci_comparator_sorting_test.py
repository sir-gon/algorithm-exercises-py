import unittest
from pathlib import Path

from ....hackerrank.lib.loader import load_test_cases
from .ctci_comparator_sorting import Player, SortablePlayer, comparator_sorting

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = load_test_cases(FILE_PATH + '/ctci_comparator_sorting.testcases.json')


class TestComparatorSorting(unittest.TestCase):
    def test_player(self):

        a_player = Player('David', 100)
        a_as_string = str(a_player)
        a_answer = ''

        self.assertEqual(a_as_string, a_answer)

        b_player = Player('Kurt', 10)
        comparator_answer = 0
        self.assertEqual(a_player.comparator(b_player), comparator_answer)

    def test_comparator_sorting(self):

        for _, _tt in enumerate(TEST_CASES):

            players: list[SortablePlayer] = []

            for __, player in enumerate(_tt['input']):
                players.append(SortablePlayer(player['name'], player['score']))

            self.assertEqual(
                comparator_sorting(players), _tt['expected'],
                f"{_} | comparator_sorting({_tt['input']}) must be "
                f"=> {_tt['expected']}")
