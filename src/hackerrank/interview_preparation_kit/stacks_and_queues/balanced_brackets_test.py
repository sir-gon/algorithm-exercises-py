import unittest

from .balanced_brackets import is_balanced


TEST_CASES = [
    {
        'title': 'Sample Test Case 0',
        'tests':
        [
            {
                'input': '{[()]}',
                'answer': True
            },
            {
                'input': '{[(])}',
                'answer': False
            },
            {
                'input': '{{[[(())]]}}',
                'answer': True
            }
        ]
    },
    {
        'title': 'Sample Test Case 1',
        'tests':
        [
            {
                'input': '{{([])}}',
                'answer': True
            },
            {
                'input': '{{)[](}}',
                'answer': False
            }
        ]
    },
    {
        'title': 'Sample Test Case 1',
        'tests':
        [
            {
                'input': '{(([])[])[]}',
                'answer': True
            },
            {
                'input': '{(([])[])[]]}',
                'answer': False
            },
            {
                'input': '{(([])[])[]}[]',
                'answer': True
            }
        ]
    }
]


class TestBalancedBrackets(unittest.TestCase):

    def test_is_balanced(self):

        for _, testset in enumerate(TEST_CASES):

            for _, _tt in enumerate(testset['tests']):

                self.assertEqual(
                    is_balanced(_tt['input']), _tt['answer'],
                    f"{_} | is_balanced({_tt['input']}) must be "
                    f"=> {_tt['answer']}")
