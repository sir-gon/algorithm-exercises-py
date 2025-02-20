import unittest
from pathlib import Path

from ....lib.loader import loadTestCases
from .ctci_comparator_sorting import Player, SortablePlayer, comparatorSorting

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = loadTestCases(FILE_PATH + '/ctci_comparator_sorting.testcases.json')


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
                comparatorSorting(players), _tt['expected'],
                f"{_} | comparatorSorting({_tt['input']}) must be "
                f"=> {_tt['expected']}")
