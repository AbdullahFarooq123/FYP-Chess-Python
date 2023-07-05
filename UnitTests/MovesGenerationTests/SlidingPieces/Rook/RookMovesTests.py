from FenUtilities.FenDecrypt import decrypt_fen
from FenUtilities.FenModel import Fen
from MoveGenerationUtilities.GenerateMovesEngine.GenerateMoves import get_rook_moves
from MoveGenerationUtilities.GenerateMovesEngine.MoveGenerationModels.MovesModel import GameStateModel
from UnitTests.MovesGenerationTests.MovesEncryptionModel import encrypt_move
from UnitTests.MovesGenerationTests.SlidingPieces.Rook.RookTestsData import white_rook_test_data
from UnitTests.UnitTestDependencies import assert_case
from UnitTests.UnitTestModels.UnitTestDataModel import UTestDataModel
from UnitTests.UnitTestModels.UnitTestModel import UnitTest
from UnitTests.UnitTestModels.UnitTestSectionModel import UTestSectionModel


def run_rook_moves_tests() -> UTestSectionModel:
    white_moves_length_test = rook_moves_length_tests()
    white_moves_generation_test = rook_moves_tests()
    return UTestSectionModel('Rook Moves Tests',
                             [white_moves_length_test, white_moves_generation_test])


def rook_moves_length_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, (fen, tested_values) in enumerate(white_rook_test_data.items()):
        fen_model: Fen = decrypt_fen(fen)
        move_model = GameStateModel(fen_model)
        moves_list_len = str(len(get_rook_moves(move_model)))
        tested_values_len = str(len(tested_values))
        unit_tests.append(
            assert_case(tested_values_len, moves_list_len, index + 1))
    return UTestDataModel(test_case_title='Rook Move Count Tests', test_cases=unit_tests)


def rook_moves_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    index: int = 1
    for fen, tested_values in white_rook_test_data.items():
        fen_model: Fen = decrypt_fen(fen)
        move_model = GameStateModel(fen_model)
        generated_moves = get_rook_moves(move_model)
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
    return UTestDataModel(test_case_title='Rook Move Generation Tests', test_cases=unit_tests)
