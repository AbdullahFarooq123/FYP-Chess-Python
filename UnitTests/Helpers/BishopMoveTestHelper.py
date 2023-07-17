from src.Helpers.FenHelpers.FenDecryptHelpers import decrypt_fen
from src.Models.FenModel import Fen
from src.Helpers.GenerateMoveHelpers.Bishop import get_bishop_moves
from src.Models.GameStateModel import GameState
from UnitTests.Helpers.MoveEncryptionHelper import encrypt_move
from UnitTests.TestData.BishopTestData import bishop_move_generations
from UnitTests.Helpers.UnitTestHelpers import assert_case
from UnitTests.Models.UnitTestDataModel import UTestDataModel
from UnitTests.Models.UnitTestModel import UnitTest
from UnitTests.Models.UnitTestSectionModel import UTestSectionModel


def run_bishop_moves_tests() -> UTestSectionModel:
    white_moves_length_test = bishop_moves_length_tests()
    white_moves_generation_test = bishop_moves_tests()
    return UTestSectionModel('Bishop Moves Tests',
                             [white_moves_length_test, white_moves_generation_test])


def bishop_moves_length_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, (fen, tested_values) in enumerate(bishop_move_generations.items()):
        fen_model: Fen = decrypt_fen(fen)
        move_model = GameState(fen_model)
        moves_list_len = str(len(get_bishop_moves(move_model)))
        tested_values_len = str(len(tested_values))
        unit_tests.append(
            assert_case(tested_values_len, moves_list_len, index + 1))
    return UTestDataModel(test_case_title='Bishop Move Count Tests', test_cases=unit_tests)


def bishop_moves_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    index: int = 1
    for fen, tested_values in bishop_move_generations.items():
        fen_model: Fen = decrypt_fen(fen)
        move_model = GameState(fen_model)
        generated_moves = get_bishop_moves(move_model)
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
    return UTestDataModel(test_case_title='Bishop Move Generation Tests', test_cases=unit_tests)
