import unittest
import json
from pathlib import Path
from typing import Dict

from .ctci_recursive_staircase import step_perms, step_perms_comput_with_cache
from .ctci_recursive_staircase_alternative import step_perms as step_perms_alt

FILE_PATH = str(Path(__file__).resolve().parent)

with open(
        FILE_PATH +
        '/ctci_recursive_staircase.testcases.json',
        encoding="utf-8"
        ) as file1:
    TEST_CASES = json.load(file1)

with open(
        FILE_PATH +
        '/ctci_recursive_staircase_generalized.testcases.json',
        encoding="utf-8"
        ) as file2:
    TEST_CASES_GENERALIZED = json.load(file2)


class TestStaircase(unittest.TestCase):

    def test_step_perms_alt_edge_case(self):

        n_input: int = 0
        answer: int = 0
        title: str = 'Edge Case 0'

        self.assertEqual(
            step_perms(n_input), answer,
            f"step_perms_alt({input}) must be "
            f"=> {answer} in {title}")

    def test_step_perms(self):

        for _, testset in enumerate(TEST_CASES):

            for _, _tt in enumerate(testset['tests']):

                self.assertEqual(
                    step_perms(_tt['input']), _tt['expected'],
                    f"{_} | step_perms({_tt['input']}) must be "
                    f"=> {_tt['expected']} in {testset['title']}")

    def test_step_perms_comput_with_cache(self):

        for _, testset in enumerate(TEST_CASES_GENERALIZED):

            for _, _tt in enumerate(testset['tests']):

                initial_cache: Dict[int, int] = {}

                self.assertEqual(
                    step_perms_comput_with_cache(
                        _tt['input'], initial_cache,
                        _tt['limit']),
                    _tt['expected'],
                    f"{_} | step_perms_comput_with_cache("
                    f"{_tt['input']}, {initial_cache}, {_tt['limit']}) must be "
                    f"=> {_tt['expected']} in {testset['title']}")

    def test_step_perms_alt(self):

        for _, testset in enumerate(TEST_CASES):

            for _, _tt in enumerate(testset['tests']):

                self.assertEqual(
                    step_perms_alt(_tt['input']), _tt['expected'],
                    f"{_} | step_perms_alt({_tt['input']}) must be "
                    f"=> {_tt['expected']} in {testset['title']}")
