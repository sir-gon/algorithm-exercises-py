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

    def add(self, point_a: int):
        if point_a not in self._friendship:
            self._friendship[point_a] = -1

    def find(self, point_a: int) -> int:
        if self._friendship[point_a] < 0:
            return point_a
        return self.find(self._friendship[point_a])

    def unite(self, point_a: int, point_b: int) -> bool:

        self.add(point_a)
        self.add(point_b)

        _a = self.find(point_a)
        _b = self.find(point_b)

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


def maxCircle(queries) -> list[int]:
    result: list[int] = []
    friends = GroupingFriends()

    for query in queries:
        # Computing friendship
        friends.unite(query[0], query[1])

        # Counting friends groups
        result.append(friends.count_groups())

    return result
