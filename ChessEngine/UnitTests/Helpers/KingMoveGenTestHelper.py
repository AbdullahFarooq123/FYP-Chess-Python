from ChessEngine.UnitTests.TestData.KingTestData import king_attacks
from ChessEngine.src.Helpers.BeautifyHelpers.GameBeautifyHelpers import get_binary
from ChessEngine.src.Enums.PositionsEnum import Positions

from ChessEngine.src.Helpers.PreCalculationHelpers.KingPreCalHelpers import get_king_attack
from ChessEngine.src.Root.PreCalculationsData import king_attack_maps
from ChessEngine.UnitTests.Helpers.UnitTestHelpers import flatten_position, assert_case
from ChessEngine.UnitTests.Models.UnitTestDataModel import UTestDataModel
from ChessEngine.UnitTests.Models.UnitTestModel import UnitTest
from ChessEngine.UnitTests.Models.UnitTestSectionModel import UTestSectionModel


def run_king_tests() -> UTestSectionModel:
    attacks_generation_model = king_attacks_generation_test()
    attacks_generated_model = king_attacks_generated_test()
    return UTestSectionModel('King Tests', [attacks_generation_model, attacks_generated_model])


def king_attacks_generation_test() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_king_attack_mask = get_binary(get_king_attack(position.value))
        tested_king_attack_mask = flatten_position(king_attacks[position.name])
        unit_tests.append(
            assert_case(tested_king_attack_mask, calculated_king_attack_mask, index + 1))
    return UTestDataModel(test_case_title='King Attacks Generation Tests', test_cases=unit_tests)


def king_attacks_generated_test() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_king_attack_mask = get_binary(king_attack_maps[position.value])
        tested_king_attack_mask = flatten_position(king_attacks[position.name])
        unit_tests.append(
            assert_case(tested_king_attack_mask, calculated_king_attack_mask, index + 1))
    return UTestDataModel(test_case_title='King Attacks Generated Tests', test_cases=unit_tests)
