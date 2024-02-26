import unittest

from .sherlock_and_anagrams import sherlock_and_anagrams


TEST_CASES = [
    {
        'title': 'Sample Test Case 0',
        'tests':
        [
            {
                'input': 'abba',
                'answer': 4
            },
            {
                'input': 'abcd',
                'answer': 0
            }
        ]
    },
    {
        'title': 'Sample Test Case 1',
        'tests':
        [
            {
                'input': 'ifailuhkqq',
                'answer': 3
            },
            {
                'input': 'kkkk',
                'answer': 10
            }
        ]
    },
    {
        'title': 'Sample Test Case 1',
        'tests':
        [
            {
                'input': 'cdcd',
                'answer': 5
            }
        ]
    }
]


class TestBubleSort(unittest.TestCase):

    def test_sorts(self):

        for _, testset in enumerate(TEST_CASES):

            for _, _tt in enumerate(testset['tests']):

                self.assertEqual(
                    sherlock_and_anagrams(_tt['input']), _tt['answer'],
                    f"{_} | sherlock_and_anagrams({_tt['input']}) must be "
                    f"=> {_tt['answer']}")
