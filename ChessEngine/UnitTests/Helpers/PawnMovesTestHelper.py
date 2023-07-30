from ChessEngine.src.Helpers.FenHelpers.FenDecryptHelpers import decrypt_fen
from ChessEngine.src.Models.FenModel import Fen
from ChessEngine.src.Controllers.GenerateMovesController import get_white_pawn_moves, get_black_pawn_moves
from ChessEngine.src.Models.GameStateModel import GameState
from ChessEngine.UnitTests.Helpers.MoveEncryptionHelper import encrypt_move
from ChessEngine.UnitTests.TestData.PawnTestData import white_pawn, black_pawn
from ChessEngine.UnitTests.Helpers.UnitTestHelpers import assert_case
from ChessEngine.UnitTests.Models.UnitTestDataModel import UTestDataModel
from ChessEngine.UnitTests.Models.UnitTestModel import UnitTest
from ChessEngine.UnitTests.Models.UnitTestSectionModel import UTestSectionModel


def run_pawn_moves_tests() -> UTestSectionModel:
    white_moves_length_test = white_pawn_moves_length_tests()
    white_moves_generation_test = white_pawn_moves_tests()
    black_moves_length_test = black_pawn_moves_length_tests()
    black_moves_generation_test = black_pawn_moves_tests()
    return UTestSectionModel('Pawn Moves Tests',
                             [white_moves_length_test, white_moves_generation_test, black_moves_length_test,
                              black_moves_generation_test])


def white_pawn_moves_length_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, (fen, tested_values) in enumerate(white_pawn.items()):
        fen_model: Fen = decrypt_fen(fen)
        move_model = GameState(fen_model)
        moves_list_len = str(len(get_white_pawn_moves(move_model)))
        tested_values_len = str(len(tested_values))
        unit_tests.append(
            assert_case(tested_values_len, moves_list_len, index + 1))
    return UTestDataModel(test_case_title='White Pawn Move Count Tests', test_cases=unit_tests)


def white_pawn_moves_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    index: int = 1
    for fen, tested_values in white_pawn.items():
        fen_model: Fen = decrypt_fen(fen)
        move_model = GameState(fen_model)
        generated_moves = get_white_pawn_moves(move_model)
        tested_moves = [encrypt_move(move) for move in tested_values]
        for tested_move in tested_moves:
            found: bool = False
            for generated_move in generated_moves:
                if tested_move == generated_move:
                    unit_tests.append(
                        assert_case(str(tested_move), str(generated_move), index))
                    index += 1
                    found = True
                    break
            if not found:
                unit_tests.append(
                    assert_case(str(tested_move), '', index))
                index += 1
    return UTestDataModel(test_case_title='White Pawn Move Generation Tests', test_cases=unit_tests)


def black_pawn_moves_length_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, (fen, tested_values) in enumerate(black_pawn.items()):
        fen_model: Fen = decrypt_fen(fen)
        move_model = GameState(fen_model)
        moves_list_len = str(len(get_black_pawn_moves(move_model)))
        tested_values_len = str(len(tested_values))
        unit_tests.append(
            assert_case(moves_list_len, tested_values_len, index + 1))
    return UTestDataModel(test_case_title='Black Pawn Move Count Tests', test_cases=unit_tests)


def black_pawn_moves_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    index: int = 1
    for fen, tested_values in black_pawn.items():
        fen_model: Fen = decrypt_fen(fen)
        move_model = GameState(fen_model)
        generated_moves = get_black_pawn_moves(move_model)
        tested_moves = [encrypt_move(move) for move in tested_values]
        for tested_move in tested_moves:
            found: bool = False
            for generated_move in generated_moves:
                if tested_move == generated_move:
                    unit_tests.append(
                        assert_case(str(tested_move), str(generated_move), index))
                    index += 1
                    found = True
                    break
            if not found:
                unit_tests.append(
                    assert_case(str(tested_move), '', index))
                index += 1
    return UTestDataModel(test_case_title='Black Pawn Move Generation Tests', test_cases=unit_tests)
