from ChessEngine.UnitTests.Helpers.BlackKingCastleMoveTestHelper import black_king_castle_moves_length_tests, \
    black_king_castle_moves_generation_tests
from ChessEngine.UnitTests.Helpers.WhiteKingCastleMoveTestHelper import white_king_castle_moves_length_tests, \
    white_king_castle_moves_generation_tests
from ChessEngine.UnitTests.Helpers.KingNormalMoveTestHelper import king_moves_length_tests, \
    king_moves_generation_tests
from ChessEngine.UnitTests.Models.UnitTestSectionModel import UTestSectionModel


def run_king_moves_tests() -> UTestSectionModel:
    white_castle_moves_length_test = white_king_castle_moves_length_tests()
    white_castle_moves_generation_test = white_king_castle_moves_generation_tests()
    black_castle_moves_length_test = black_king_castle_moves_length_tests()
    black_castle_moves_generation_test = black_king_castle_moves_generation_tests()
    king_normal_moves_length_test = king_moves_length_tests()
    king_normal_moves_generation_test = king_moves_generation_tests()
    return UTestSectionModel('King Moves Tests', [white_castle_moves_length_test, white_castle_moves_generation_test,
                                                  black_castle_moves_length_test, black_castle_moves_generation_test,
                                                  king_normal_moves_length_test, king_normal_moves_generation_test])
