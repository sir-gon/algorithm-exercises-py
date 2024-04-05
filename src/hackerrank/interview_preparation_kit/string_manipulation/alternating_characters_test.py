import unittest
from .alternating_characters import alternating_characters

TEST_CASES = [
    {
        'title': 'Sample Test case 0',
        'tests': [
            {
                'input': 'AAAA',
                'answer': 3
            },
            {
                'input': 'BBBBB',
                'answer': 4
            },
            {
                'input': 'ABABABAB',
                'answer': 0
            },
            {
                'input': 'BABABA',
                'answer': 0
            },
            {
                'input': 'AAABBB',
                'answer': 4
            }
        ]
    },
    {
        'title': 'Sample Test case 13',
        'tests': [
            {
                'input': 'AAABBBAABB',
                'answer': 6
            },
            {
                'input': 'AABBAABB',
                'answer': 4
            },
            {
                'input': 'ABABABAA',
                'answer': 1
            }
        ]
    },
    {
        'title': 'Sample Test case 14',
        'tests': [
            {
                'input': 'ABBABBAA',
                'answer': 3
            }
        ]
    }
]


class TestAlternatingCharacters(unittest.TestCase):

    def test_alternating_characters(self):

        for _, testset in enumerate(TEST_CASES):

            for _, _tt in enumerate(testset['tests']):

                self.assertEqual(
                    alternating_characters(_tt['input']), _tt['answer'],
                    f"{_} | alternating_characters({_tt['input']}) must be "
                    f"=> {_tt['answer']}")
