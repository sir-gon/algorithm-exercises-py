import unittest
from pathlib import Path
from typing import Dict

from ....lib.loader import loadTestCases
from .ctci_recursive_staircase import stepPerms, stepPermsComputWithCache
from .ctci_recursive_staircase_alternative import stepPerms as stepPermsAlt

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = loadTestCases(
    FILE_PATH + '/ctci_recursive_staircase.testcases.json')

TEST_CASES_GENERALIZED = loadTestCases(
    FILE_PATH + '/ctci_recursive_staircase_generalized.testcases.json')


class TestStaircase(unittest.TestCase):

    def test_step_perms_alt_edge_case(self):

        n_input: int = 0
        answer: int = 0
        title: str = 'Edge Case 0'

        self.assertEqual(
            stepPermsAlt(n_input), answer,
            f"stepPermsAlt({input}) must be "
            f"=> {answer} in {title}")

    def test_step_perms(self):

        for _, testset in enumerate(TEST_CASES):

            for _, _tt in enumerate(testset['tests']):

                self.assertEqual(
                    stepPerms(_tt['input']), _tt['expected'],
                    f"{_} | stepPerms({_tt['input']}) must be "
                    f"=> {_tt['expected']} in {testset['title']}")

    def test_step_perms_comput_with_cache(self):

        for _, testset in enumerate(TEST_CASES_GENERALIZED):

            for _, _tt in enumerate(testset['tests']):

                initial_cache: Dict[int, int] = {}

                self.assertEqual(
                    stepPermsComputWithCache(
                        _tt['input'], initial_cache,
                        _tt['limit']),
                    _tt['expected'],
                    f"{_} | stepPermsComputWithCache("
                    f"{_tt['input']}, {initial_cache}, {_tt['limit']}) must be "
                    f"=> {_tt['expected']} in {testset['title']}")

    def test_step_perms_alt(self):

        for _, testset in enumerate(TEST_CASES):

            for _, _tt in enumerate(testset['tests']):

                self.assertEqual(
                    stepPermsAlt(_tt['input']), _tt['expected'],
                    f"{_} | stepPermsAlt({_tt['input']}) must be "
                    f"=> {_tt['expected']} in {testset['title']}")
