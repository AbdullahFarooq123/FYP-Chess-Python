# from NeuralNetworks.PositionEvaluatorCNN.Controllers.ProcessDataController import load_data_in_tensor, load_data
from ChessEngine.UnitTests.Controllers.GamePlayTestController import run_game_play_tests
from ChessEngine.UnitTests.Controllers.UnitTestController import UnitTestEngine
from ChessEngine.UnitTests.Enums.TestOfEnum import TestsOf
from ChessEngine.src.Controllers import PreCalculationsController
from NeuralNetworks.PositionEvaluatorCNN.Controllers.LoadDataController import load_data


def run_unit_test():
    u_engine = UnitTestEngine(show_only_tests=TestsOf.FAILED, print_test_cases=TestsOf.FAILED,
                              print_test_case_details=TestsOf.FAILED)
    u_engine.run_tests()
    u_engine.print_tests()
    run_game_play_tests()


def run_migrations():
    PreCalculationsController.init_migrations()


def run_testing():
    [input_board, input_features], input_labels = load_data(limit=1)
    print(input_board, input_features, input_labels)


if __name__ == '__main__':
    run_testing()
    # run_unit_test()
    # run_migrations()
