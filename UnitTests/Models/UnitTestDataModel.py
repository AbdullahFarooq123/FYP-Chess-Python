from UnitTests.Enums.TestOfEnum import TestsOf
from src.Helpers.BeautifyHelpers.StringBeautifyHelpers import print_by_padding, Justify
from UnitTests.Models.UnitTestModel import UnitTest


class UTestDataModel:
    def __init__(self, test_case_title: str, test_cases: list[UnitTest]):
        self.test_case_title = test_case_title
        self.test_cases = test_cases
        self.sub_part_id = 1
        self.padding_length = 100

    def get_validated_tests(self, validate_test_of: TestsOf) -> list[UnitTest]:
        return [test for test in self.test_cases if test.passed in validate_test_of.value]

    def print_data(self, print_test_cases: TestsOf = TestsOf.NONE, print_test_case_detail: TestsOf = TestsOf.NONE):
        print_by_padding(string=f'{"Failed" if any(not test.passed for test in self.test_cases) else "Passed"}',
                         length=self.padding_length, sub_part=self.sub_part_id)
        print_by_padding(string='', length=self.padding_length, start_end_only=True, sub_part=self.sub_part_id)
        print_by_padding(
            string=f' Title : {self.test_case_title}',
            length=self.padding_length, start_end_only=True, justify=Justify.LEFT, sub_part=self.sub_part_id)
        print_by_padding(
            string=f' Test Cases : {len(self.test_cases)}',
            length=self.padding_length, start_end_only=True, justify=Justify.LEFT, sub_part=self.sub_part_id)
        print_by_padding(
            string=f' {sum(test_case.passed for test_case in self.test_cases)} test cases passed!',
            length=self.padding_length, start_end_only=True, justify=Justify.LEFT, sub_part=self.sub_part_id)
        print_by_padding(
            string=f' {sum(not test_case.passed for test_case in self.test_cases)} test cases failed!',
            length=self.padding_length, start_end_only=True, justify=Justify.LEFT, sub_part=self.sub_part_id)
        print_by_padding(string='', length=self.padding_length, start_end_only=True, sub_part=self.sub_part_id)
        validated_test_cases = self.get_validated_tests(print_test_cases)
        if len(validated_test_cases) > 0:
            print_by_padding(string='Test Cases', length=self.padding_length, sub_part=self.sub_part_id + 1)
            print_by_padding(string='', length=self.padding_length, start_end_only=True, sub_part=self.sub_part_id + 1)
            for test_case in validated_test_cases:
                print_by_padding(
                    string=f' Case {test_case.case_id} : {"Passed" if test_case.passed else "Not Passed"}',
                    length=self.padding_length, start_end_only=True, justify=Justify.LEFT,
                    sub_part=self.sub_part_id + 1)
                if test_case.passed in print_test_case_detail.value:
                    test_case.print_data(sub_part_id=self.sub_part_id + 1, padding_length=self.padding_length,
                                         justify=Justify.LEFT)
            print_by_padding(string='', length=self.padding_length, start_end_only=True, sub_part=self.sub_part_id + 1)
            print_by_padding(string=f'', length=self.padding_length, sub_part=self.sub_part_id + 1)
            print_by_padding(string='', length=self.padding_length, start_end_only=True, sub_part=self.sub_part_id)

        print_by_padding(string=f'', length=self.padding_length, sub_part=self.sub_part_id)
