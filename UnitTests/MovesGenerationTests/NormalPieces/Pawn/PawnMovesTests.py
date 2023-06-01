from DebugUtilities.BeautifyDependency.GameBeautify import print_bitboard, print_game_board
from FenUtilities.FenDecrypt import decryptFen
from FenUtilities.FenModel import Fen
from MoveGenerationUtilities.GenerateMovesEngine.GenerateMoves import get_white_pawn_moves
from MoveGenerationUtilities.GenerateMovesEngine.MovesModel import MoveDependencyModel
from UnitTests.MovesGenerationTests.MovesEncryptionModel import encrypt_move
from UnitTests.MovesGenerationTests.NormalPieces.Pawn.PawnTestsData import white_test_data, black_test_data
from UnitTests.UnitTestDependencies import assert_case
from UnitTests.UnitTestModels.UnitTestDataModel import UTestDataModel
from UnitTests.UnitTestModels.UnitTestModel import UnitTest
from UnitTests.UnitTestModels.UnitTestSectionModel import UTestSectionModel


def run_pawn_moves_tests() -> UTestSectionModel:
    moves_length_test = white_pawn_moves_length_tests()
    moves_generation_test = white_pawn_moves_tests()
    return UTestSectionModel('Pawn Moves Tests', [moves_length_test, moves_generation_test])


def white_pawn_moves_length_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, (fen, tested_values) in enumerate(white_test_data.items()):
        fen_model: Fen = decryptFen(fen)
        move_model = MoveDependencyModel(fen_model, 0)
        moves_list_len = str(len(get_white_pawn_moves(move_model)))
        tested_values_len = str(len(tested_values))
        unit_tests.append(
            assert_case(tested_values_len, moves_list_len, index + 1))
    return UTestDataModel(test_case_title='White Pawn Move Count Tests', test_cases=unit_tests)


def white_pawn_moves_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    index: int = 1
    for fen, tested_values in white_test_data.items():
        fen_model: Fen = decryptFen(fen)
        move_model = MoveDependencyModel(fen_model, 0)
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
    for index, (fen, tested_values) in enumerate(black_test_data.items()):
        fen_model: Fen = decryptFen(fen)
        move_model = MoveDependencyModel(fen_model, 0)
        moves_list_len = str(len(get_white_pawn_moves(move_model)))
        tested_values_len = str(len(tested_values))
        unit_tests.append(
            assert_case(moves_list_len, tested_values_len, index + 1))
    return UTestDataModel(test_case_title='Black Pawn Move Count Tests', test_cases=unit_tests)


def black_pawn_moves_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    index: int = 1
    for fen, tested_values in black_test_data.items():
        fen_model: Fen = decryptFen(fen)
        move_model = MoveDependencyModel(fen_model, 0)
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
    return UTestDataModel(test_case_title='Black Pawn Move Generation Tests', test_cases=unit_tests)