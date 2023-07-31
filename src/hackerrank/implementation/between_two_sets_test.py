import unittest
from .between_two_sets import get_total_x, is_factor, factor_of


class TestProblemBetweenTwoSets(unittest.TestCase):

    def test_get_total_x(self):

        tinput: list[int] = [16, 32, 96]
        solution_found: int = 0

        calculated_a = get_total_x([], tinput)

        self.assertEqual(
            calculated_a, solution_found,
            f"get_total_x([], tinput) must be "
            f"=> {solution_found}")

        calculated_b = get_total_x(tinput, [])

        self.assertEqual(
            calculated_b, solution_found,
            f"get_total_x({tinput}, {[]}) must be "
            f"=> {solution_found}")

        calculated_c = get_total_x([], [])

        self.assertEqual(
            calculated_c, solution_found,
            f"get_total_x({[]}, {[]}) must be "
            f"=> {solution_found}")

        calculated_d = is_factor(1, [])

        self.assertEqual(
            calculated_d, solution_found,
            f"is_factor({1}, {[]}) must be "
            f"=> {False}")

        calculated_e = factor_of(1, [])

        self.assertEqual(
            calculated_e, solution_found,
            f"factor_of({1}, {[]}) must be "
            f"=> {False}")

    def test_get_total_x_case_0(self):

        _a_ = [2, 4]
        _b_ = [16, 32, 96]
        _b_reverse_ = [96, 32, 16]

        solution_found = 3

        self.assertEqual(
            get_total_x(_a_, _b_), solution_found,
            f"get_total_x({_a_}, {_b_}) must be "
            f"=> {solution_found}")

        self.assertEqual(
            get_total_x(_a_, _b_reverse_), solution_found,
            f"get_total_x({_a_}, {_b_reverse_}) must be "
            f"=> {solution_found}")
