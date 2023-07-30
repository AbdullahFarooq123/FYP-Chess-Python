from ChessEngine.UnitTests.TestData.KingTestData import white_king_castle
from ChessEngine.src.Helpers.FenHelpers.FenDecryptHelpers import decrypt_fen
from ChessEngine.src.Models.FenModel import Fen
from ChessEngine.src.Controllers.GenerateMovesController import get_white_castle_moves
from ChessEngine.src.Models.GameStateModel import GameState
from ChessEngine.UnitTests.Helpers.MoveEncryptionHelper import encrypt_move
from ChessEngine.UnitTests.Helpers.UnitTestHelpers import assert_case
from ChessEngine.UnitTests.Models.UnitTestDataModel import UTestDataModel
from ChessEngine.UnitTests.Models.UnitTestModel import UnitTest


def white_king_castle_moves_length_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, (fen, tested_values) in enumerate(white_king_castle.items()):
        fen_model: Fen = decrypt_fen(fen)
        move_model = GameState(fen_model)
        moves_list_len = str(len(get_white_castle_moves(move_model)))
        tested_values_len = str(len(tested_values))
        unit_tests.append(
            assert_case(tested_values_len, moves_list_len, index + 1))
    return UTestDataModel(test_case_title='White King Castle Move Count Tests', test_cases=unit_tests)


def white_king_castle_moves_generation_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    index: int = 1
    for fen, tested_values in white_king_castle.items():
        fen_model: Fen = decrypt_fen(fen)
        move_model = GameState(fen_model)
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
