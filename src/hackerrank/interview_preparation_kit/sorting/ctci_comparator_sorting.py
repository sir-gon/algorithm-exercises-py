from __future__ import annotations
from typing import List

# Given Code
from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        # Given code
        pass

    def __repr__(self):
        # Given code
        return ''

    def comparator(self, b):
        # Given code
        pass

# End Given code


class SortablePlayer(Player):
    name: str = ''
    score: int = 0

    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score

    def __repr__(self) -> str:
        return f'{self.name} {self.score}'

    def comparator(self: SortablePlayer, b: SortablePlayer):
        if self.score > b.score:
            return -1
        if self.score < b.score:
            return 1
        if self.name < b.name:
            return -1
        if self.name > b.name:
            return 1

        return 0


def comparator_sorting(data: List[SortablePlayer]) -> str:

    data = sorted(data, key=cmp_to_key(SortablePlayer.comparator))

    output: List[str] = []
    for x in data:
        output.append(str(x))

    return '\n'.join(output)
