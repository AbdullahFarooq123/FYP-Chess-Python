from ChessEngine.UnitTests.Controllers.GamePlayTestController import run_game_play_tests
from ChessEngine.UnitTests.Controllers.UnitTestController import UnitTestEngine
from ChessEngine.UnitTests.Enums.TestOfEnum import TestsOf
from ChessEngine.src.Controllers import PreCalculationsController


def run_unit_test():
    u_engine = UnitTestEngine(show_only_tests=TestsOf.FAILED, print_test_cases=TestsOf.FAILED,
                              print_test_case_details=TestsOf.FAILED)
    u_engine.run_tests()
    u_engine.print_tests()
    run_game_play_tests()


def run_migrations():
    PreCalculationsController.init_migrations()


def run_testing():
    pass


if __name__ == '__main__':
    run_testing()
    # run_unit_test()
    # run_migrations()
