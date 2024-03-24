import unittest

from .ctci_ice_cream_parlor import what_flavors


TEST_CASES = [
    {
        'title': 'Sample Test Case 0',
        'tests':
        [
            {
                'costs': [1, 4, 5, 3, 2],
                'money': 4,
                'answer': [1, 4]
            },
            {
                'costs': [2, 2, 4, 3],
                'money': 4,
                'answer': [1, 2]
            }
        ]
    },
    {
        'title': 'Sample Test Case 1',
        'tests':
        [
            {
                'costs': [1, 2, 3, 5, 6],
                'money': 5,
                'answer': [2, 3]
            }
        ]
    },
    {
        'title': 'Sample Test Case 2',
        'tests':
        [
            {
                'costs': [4, 3, 2, 5, 7],
                'money': 8,
                'answer': [2, 4]
            },
            {
                'costs': [7, 2, 5, 4, 11],
                'money': 12,
                'answer': [1, 3]
            }
        ]
    }
]


class TestIceCreamParlor(unittest.TestCase):

    def test_what_flavors(self):

        for _, testset in enumerate(TEST_CASES):

            for _, _tt in enumerate(testset['tests']):

                self.assertEqual(
                    what_flavors(_tt['costs'], _tt['money']), _tt['answer'],
                    f"{_} | what_flavors({_tt['costs']}, {_tt['money']}) must be "
                    f"=> {_tt['answer']}")
