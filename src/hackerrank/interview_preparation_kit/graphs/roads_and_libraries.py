# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/graphs/roads_and_libraries.md]]


class RoadsAndLibraries:

    _paths = []
    _unions = 0

    def __init__(self, q_paths: int, cities: list[list[int]]):

        self._paths = [-1 for _ in range(q_paths + 1)]

        for path in cities:
            city_a, city_b = path[0], path[1]
            if self.unite(city_a, city_b):
                self._unions += 1

    def find(self, point_a: int):
        if self._paths[point_a] < 0:
            return point_a
        return self.find(self._paths[point_a])

    def unite(self, _point_a: int, _point_b: int) -> bool:
        point_a = self.find(_point_a)
        point_b = self.find(_point_b)
        if point_a == point_b:
            return False
        if self._paths[point_a] > self._paths[point_b]:
            point_a, point_b = point_b, point_a
        self._paths[point_a] += self._paths[point_b]
        self._paths[point_b] = point_a
        return True

    def get_unions(self) -> int:
        return self._unions


def roads_and_libraries(
        q_paths: int,
        c_lib: int,
        c_road: int,
        cities: list[list[int]]) -> int:

    ral = RoadsAndLibraries(q_paths, cities)
    unions = ral.get_unions()

    ans1 = c_lib * q_paths
    ans2 = c_road * unions + c_lib * (q_paths - unions)
    return min(ans1, ans2)
