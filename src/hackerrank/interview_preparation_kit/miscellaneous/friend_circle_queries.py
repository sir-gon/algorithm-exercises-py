# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/miscellaneous/friend-circle-queries.md]] # noqa
# pylint: enable=line-too-long

from typing import Dict


class GroupingFriends:
    _friendship: Dict[int, int] = {}
    _large_friendship: int

    def __init__(self) -> None:
        self._friendship: Dict[int, int] = {}
        self._large_friendship = 0

    def add(self, a: int):
        if a not in self._friendship:
            self._friendship[a] = -1

    def find(self, a: int) -> int:
        return a if self._friendship[a] < 0 else self.find(self._friendship[a])

    def unite(self, a: int, b: int) -> bool:

        self.add(a)
        self.add(b)

        _a = self.find(a)
        _b = self.find(b)

        if _a == _b:
            return False

        if _a > _b:
            _a, _b = _b, _a

        self._friendship[_a] += self._friendship[_b]
        self._friendship[_b] = _a

        # large group is the root node with "high" value
        self._large_friendship = max(self._large_friendship, -1 * self._friendship[_a])
        return True

    def count_groups(self) -> int:
        return self._large_friendship


def max_circle(queries) -> list[int]:
    result: list[int] = []
    friends = GroupingFriends()

    for x in queries:
        # Computing friendship
        friends.unite(x[0], x[1])

        # Counting friends groups
        result.append(friends.count_groups())

    return result
