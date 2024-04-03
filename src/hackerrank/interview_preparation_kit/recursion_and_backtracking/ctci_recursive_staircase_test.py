import unittest
from .ctci_recursive_staircase import step_perms
from .ctci_recursive_staircase_alternative import step_perms as step_perms_alt

TEST_CASES = [
    {
        'title': 'Sample Test case 0',
        'tests': [
            {
                'input': 1,
                'answer': 1
            },
            {
                'input': 3,
                'answer': 4
            },
            {
                'input': 7,
                'answer': 44
            }
        ]
    },
    {
        'title': 'Sample Test case 9',
        'tests': [
            {
                'input': 5,
                'answer': 13
            },
            {
                'input': 8,
                'answer': 81
            }
        ]
    },
    {
        'title': 'Sample Test case 10',
        'tests': [
            {
                'input': 15,
                'answer': 5768
            },
            {
                'input': 20,
                'answer': 121415
            },
            {
                'input': 27,
                'answer': 8646064
            }
        ]
    }
]


class TestRecursionFibonacciNumbers(unittest.TestCase):

    def test_step_perms_alt_edge_case(self):

        n: int = 0
        answer: int = 0
        title: str = 'Edge Case 0'

        self.assertEqual(
            step_perms(n), answer,
            f"step_perms_alt({input}) must be "
            f"=> {answer} in {title}")

    def test_step_perms(self):

        for _, testset in enumerate(TEST_CASES):

            for _, _tt in enumerate(testset['tests']):

                self.assertEqual(
                    step_perms(_tt['input']), _tt['answer'],
                    f"{_} | step_perms({_tt['input']}) must be "
                    f"=> {_tt['answer']} in {testset['title']}")

    def test_step_perms_alt(self):

        for _, testset in enumerate(TEST_CASES):

            for _, _tt in enumerate(testset['tests']):

                self.assertEqual(
                    step_perms_alt(_tt['input']), _tt['answer'],
                    f"{_} | step_perms_alt({_tt['input']}) must be "
                    f"=> {_tt['answer']} in {testset['title']}")
