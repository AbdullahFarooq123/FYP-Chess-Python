from DebugUtilities.BeautifyDependency.GameBeautify import print_game_board
from FenUtilities.FenDecrypt import decryptFen
from FenUtilities.FenModel import Fen
from MoveGenerationUtilities.GenerateMovesEngine.GenerateMoves import get_white_pawn_moves, get_white_castle_moves
from MoveGenerationUtilities.GenerateMovesEngine.MoveGenerationModels.MovesModel import MoveDependencyModel
from UnitTests.MovesGenerationTests.MovesEncryptionModel import encrypt_move
from UnitTests.MovesGenerationTests.NormalPieces.King.KingCastleTestData import white_king_castle_test_data
from UnitTests.MovesGenerationTests.NormalPieces.Pawn.PawnTestsData import black_test_data
from UnitTests.UnitTestDependencies import assert_case
from UnitTests.UnitTestModels.UnitTestDataModel import UTestDataModel
from UnitTests.UnitTestModels.UnitTestModel import UnitTest
from UnitTests.UnitTestModels.UnitTestSectionModel import UTestSectionModel


def run_king_moves_tests() -> UTestSectionModel:
    white_castle_moves_length_test = white_king_castle_moves_length_tests()
    white_castle_moves_generation_test = white_king_castle_moves_generation_tests()
    return UTestSectionModel('King Moves Tests', [white_castle_moves_length_test, white_castle_moves_generation_test])


def white_king_castle_moves_length_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, (fen, tested_values) in enumerate(white_king_castle_test_data.items()):
        fen_model: Fen = decryptFen(fen)
        move_model = MoveDependencyModel(fen_model, 0)
        moves_list_len = str(len(get_white_castle_moves(move_model)))
        tested_values_len = str(len(tested_values))
        if moves_list_len != tested_values_len:
            print()
        unit_tests.append(
            assert_case(tested_values_len, moves_list_len, index + 1))
    return UTestDataModel(test_case_title='White King Castle Move Count Tests', test_cases=unit_tests)


def white_king_castle_moves_generation_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    index: int = 1
    for fen, tested_values in white_king_castle_test_data.items():
        fen_model: Fen = decryptFen(fen)
        move_model = MoveDependencyModel(fen_model, 0)
        if fen in ['8/8/8/1r6/8/8/8/R3K2R w KQ - 0 1']:
            print_game_board(fen_model.white_board,fen_model.white_pieces,fen_model.black_board,fen_model.black_pieces)
        generated_moves = get_white_castle_moves(move_model)
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
    return UTestDataModel(test_case_title='White King Castle Move Generation Tests', test_cases=unit_tests)


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