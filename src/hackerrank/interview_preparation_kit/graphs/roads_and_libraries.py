# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/graphs/roads_and_libraries.md]]


class RoadsAndLibraries:

    _paths = []
    _unions = 0

    def __init__(self, n: int, cities: list[list[int]]):

        self._paths = [-1 for _ in range(n + 1)]

        for path in cities:
            city_a, city_b = path[0], path[1]
            if self.unite(city_a, city_b):
                self._unions += 1

    def find(self, a: int):
        return a if self._paths[a] < 0 else self.find(self._paths[a])

    def unite(self, a: int, b: int) -> bool:
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self._paths[a] > self._paths[b]:
            a, b = b, a
        self._paths[a] += self._paths[b]
        self._paths[b] = a
        return True

    def get_unions(self) -> int:
        return self._unions


def roads_and_libraries(n: int, c_lib: int, c_road: int, cities: list[list[int]]) -> int:

    ral = RoadsAndLibraries(n, cities)
    unions = ral.get_unions()

    ans1 = c_lib * n
    ans2 = c_road * unions + c_lib * (n - unions)
    return min(ans1, ans2)
