# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/sort/ctci-comparator-sorting.md]]

from __future__ import annotations
from typing import List

# Given Code
from functools import cmp_to_key


class Player:
    name: str = ''
    score: int = 0

    def __init__(self, name, score):
        # Given code
        pass

    def __repr__(self) -> str:
        # Given code
        return ''

    def comparator(self, b_player: Player) -> int:
        # Given code
        return 0 * b_player.score

# End Given code


class SortablePlayer(Player):
    name: str = ''
    score: int = 0

    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score

    def __repr__(self) -> str:
        return f'{self.name} {self.score}'

    def comparator(self: Player, b_player: Player) -> int:
        if self.score > b_player.score:
            return -1
        if self.score < b_player.score:
            return 1
        if self.name < b_player.name:
            return -1
        if self.name > b_player.name:
            return 1

        return 0


def comparator_sorting(players: List[SortablePlayer]) -> str:

    players = sorted(players, key=cmp_to_key(SortablePlayer.comparator))

    output: List[str] = []
    for player in players:
        output.append(str(player))

    return '\n'.join(output)
