from ChessEngine.UnitTests.Enums.TestOfEnum import TestsOf
from ChessEngine.UnitTests.Models.UnitTestSectionModel import UTestSectionModel
from ChessEngine.UnitTests.Services import MoveGenerationTestService, PreCalculationTestService


class UnitTestEngine:
    def __init__(self, print_test_cases: TestsOf = TestsOf.NONE,
                 print_test_case_details: TestsOf = TestsOf.NONE,
                 show_only_tests: TestsOf = TestsOf.ALL):
        self.test_results: list[UTestSectionModel] = []
        self.print_test_cases = print_test_cases
        self.print_test_case_details = print_test_case_details
        self.show_only_tests = show_only_tests

    def run_tests(self):
        self.test_results += PreCalculationTestService.run_tests()
        self.test_results += MoveGenerationTestService.run_tests()

    def print_tests(self):
        for test in self.test_results:
            test.print_data(self.print_test_cases, self.print_test_case_details, self.show_only_tests)