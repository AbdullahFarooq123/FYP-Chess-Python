from enum import Enum

from UnitTests.Models.UnitTestModel import UnitTest


def flatten_position(position: str) -> str:
    return position.replace(' ', '').replace('\n', '').replace('0b', '')


def assert_case(tested_case: str, calculated_case: str, case_no: int) -> UnitTest:
    try:
        assert tested_case == calculated_case
        return UnitTest(case_id=case_no, passed=True, desired_output=tested_case, output=calculated_case)
    except AssertionError:
        return UnitTest(case_id=case_no, passed=False, desired_output=tested_case, output=calculated_case)
