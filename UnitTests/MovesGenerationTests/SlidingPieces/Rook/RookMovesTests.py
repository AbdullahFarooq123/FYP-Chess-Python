from DebugUtilities.BeautifyDependency.GameBeautify import print_fen_board
from FenUtilities.FenDecrypt import decrypt_fen
from FenUtilities.FenModel import Fen
from MoveGenerationUtilities.GenerateMovesEngine.GenerateMoves import get_white_pawn_moves, get_black_pawn_moves, \
    get_rook_moves
from MoveGenerationUtilities.GenerateMovesEngine.MoveGenerationModels.MovesModel import MoveDependencyModel
from UnitTests.MovesGenerationTests.MovesEncryptionModel import encrypt_move
from UnitTests.MovesGenerationTests.NormalPieces.Pawn.PawnTestsData import white_test_data, black_test_data
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
        move_model = MoveDependencyModel(fen_model, 0)
        # print_fen_board(fen)
        moves_list_len = str(len(get_rook_moves(move_model)))
        tested_values_len = str(len(tested_values))
        if moves_list_len != tested_values_len:
            print(fen)
        unit_tests.append(
            assert_case(tested_values_len, moves_list_len, index + 1))
    return UTestDataModel(test_case_title='Rook Move Count Tests', test_cases=unit_tests)


def rook_moves_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    index: int = 1
    for fen, tested_values in white_rook_test_data.items():
        fen_model: Fen = decrypt_fen(fen)
        if fen in ['3k4/8/8/8/8/R4n2/8/R2QK3 w - - 0 1', '3k4/8/8/8/8/6b1/6R1/3QK3 w - - 0 1',
                   '4k3/8/8/8/7b/8/5R2/4K3 w - - 0 1']:
            print_fen_board(fen)
        move_model = MoveDependencyModel(fen_model, 0)
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
