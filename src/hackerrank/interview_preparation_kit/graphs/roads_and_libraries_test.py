import unittest

from .roads_and_libraries import roads_and_libraries

TEST_CASES = [
    {
        'title': 'Sample Test Case 0 - 1',
        'n': 3,
        'c_lib': 2,
        'c_road': 1,
        'cities': [[1, 2], [3, 1], [2, 3]],
        'answer': 4
    },
    {
        'title': 'Sample Test Case 0 - 1',
        'n': 6,
        'c_lib': 2,
        'c_road': 5,
        'cities': [[1, 3], [3, 4], [2, 4], [1, 2], [2, 3], [5, 6]],
        'answer': 12
    },
    {
        'title': 'Sample Test Case 1 - 1',
        'n': 6,
        'c_lib': 2,
        'c_road': 3,
        'cities': [[1, 2], [1, 3], [4, 5], [4, 6]],
        'answer': 12
    },
    {
        'title': 'Sample Test Case 2 - 1',
        'n': 6,
        'c_lib': 2,
        'c_road': 3,
        'cities': [[1, 2], [1, 3], [4, 5], [4, 6]],
        'answer': 12
    }
]


class TestRoadsAndLibraries(unittest.TestCase):

    def test_roads_and_libraries(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                roads_and_libraries(
                    _tt['n'],
                    _tt['c_lib'],
                    _tt['c_road'],
                    _tt['cities']
                ),
                _tt['answer'],
                f"{_} | roads_and_libraries("
                f"{_tt['n']},"
                f"{_tt['c_lib']},"
                f"{_tt['c_road']},"
                f"{_tt['cities']}) must be "
                f"=> {_tt['answer']}")
