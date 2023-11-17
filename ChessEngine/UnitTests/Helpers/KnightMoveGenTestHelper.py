from ChessEngine.UnitTests.TestData.KnightTestData import knight_attacks
from ChessEngine.src.Helpers.BeautifyHelpers.GameBeautifyHelpers import get_binary
from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Helpers.PreCalculationHelpers.KnightPreCalHelpers import get_knight_attack
from ChessEngine.src.Root.PreCalculationsData import knight_attack_maps
from ChessEngine.UnitTests.Helpers.UnitTestHelpers import flatten_position, assert_case
from ChessEngine.UnitTests.Models.UnitTestDataModel import UTestDataModel
from ChessEngine.UnitTests.Models.UnitTestModel import UnitTest
from ChessEngine.UnitTests.Models.UnitTestSectionModel import UTestSectionModel


def run_knight_tests() -> UTestSectionModel:
    attacks_generation_model = knight_attacks_generation_test()
    attacks_generated_model = knight_attacks_generated_test()
    return UTestSectionModel('Knight Tests', [attacks_generation_model, attacks_generated_model])


def knight_attacks_generation_test() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_knight_attack_mask = get_binary(get_knight_attack(position.value))
        tested_knight_attack_mask = flatten_position(knight_attacks[position.name])
        unit_tests.append(
            assert_case(tested_knight_attack_mask, calculated_knight_attack_mask, index + 1))
    return UTestDataModel(test_case_title='Knight Attacks Generation Tests', test_cases=unit_tests)


def knight_attacks_generated_test() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_knight_attack_mask = get_binary(knight_attack_maps[position.value])
        tested_knight_attack_mask = flatten_position(knight_attacks[position.name])
        unit_tests.append(
            assert_case(tested_knight_attack_mask, calculated_knight_attack_mask, index + 1))
    return UTestDataModel(test_case_title='Knight Attacks Generation Tests', test_cases=unit_tests)
