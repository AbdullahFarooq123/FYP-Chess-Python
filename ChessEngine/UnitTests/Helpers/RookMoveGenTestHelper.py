from typing import List

from ChessEngine.UnitTests.TestData.RookTestData import rook_attacks_inc_ends, rook_attacks_exc_ends, rook_attack_counts
from ChessEngine.src.Helpers.BeautifyHelpers.GameBeautifyHelpers import get_binary
from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Helpers.PreCalculationHelpers.RookPreCalHelpers import \
    get_rook_attack_mask_exc_ends, get_rook_attack_mask_inc_end_blockers, get_rook_attacks
from ChessEngine.src.Helpers.PreCalculationHelpers.SliderAttackHelpers import \
    init_slider_attacks
from ChessEngine.src.Helpers.PreCalculationHelpers.BitManipulationHelpers import count_set_bits
from ChessEngine.src.Root.PreCalculationsData import rook_attacks, rook_attack_count
from ChessEngine.UnitTests.Helpers.UnitTestHelpers import assert_case, flatten_position
from ChessEngine.UnitTests.Models.UnitTestDataModel import UTestDataModel
from ChessEngine.UnitTests.Models.UnitTestModel import UnitTest
from ChessEngine.UnitTests.Models.UnitTestSectionModel import UTestSectionModel


def run_rook_tests() -> UTestSectionModel:
    attacks_exc_end_generation_model = rook_attack_exc_ends_generation_tests()
    attacks_exc_end_generated_model = rook_attack_exc_ends_generated_tests()
    attacks_inc_end_generated_model = rook_attack_inc_ends_generation_tests()
    attacks_count_generation_model = rook_attack_count_generation_tests()
    attacks_count_generated_model = rook_attack_count_generated_tests()
    attacks_generated_model = rook_attacks_table_test()

    return UTestSectionModel('Rook Tests', [attacks_exc_end_generation_model, attacks_exc_end_generated_model,
                                            attacks_inc_end_generated_model,
                                            attacks_count_generation_model, attacks_count_generated_model,
                                            attacks_generated_model])


def rook_attack_count_generation_tests() -> UTestDataModel:
    unit_tests: List[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_rook_attack_count = count_set_bits(get_rook_attack_mask_exc_ends(position))
        tested_rook_attack_mask = rook_attack_counts[position.value]
        unit_tests.append(
            assert_case(str(tested_rook_attack_mask), str(calculated_rook_attack_count), index + 1))
    return UTestDataModel(test_case_title='Rook Attacks Count Generation Tests', test_cases=unit_tests)


def rook_attack_count_generated_tests() -> UTestDataModel:
    unit_tests: List[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_rook_attack_count = rook_attack_count[position.value]
        tested_rook_attack_mask = rook_attack_counts[position.value]
        unit_tests.append(
            assert_case(str(tested_rook_attack_mask), str(calculated_rook_attack_count), index + 1))
    return UTestDataModel(test_case_title='Rook Attacks Count Generated Tests', test_cases=unit_tests)


def rook_attack_exc_ends_generation_tests() -> UTestDataModel:
    unit_tests: List[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_rook_attack_count = get_binary(get_rook_attack_mask_exc_ends(position))
        tested_rook_attack_mask = flatten_position(rook_attacks_exc_ends[position.name])
        unit_tests.append(
            assert_case(str(tested_rook_attack_mask), str(calculated_rook_attack_count), index + 1))
    return UTestDataModel(test_case_title='Rook Attacks exc. ends Generation Tests', test_cases=unit_tests)


def rook_attack_exc_ends_generated_tests() -> UTestDataModel:
    unit_tests: List[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_rook_attack_count = get_binary(rook_attacks[position.value])
        tested_rook_attack_mask = flatten_position(rook_attacks_exc_ends[position.name])
        unit_tests.append(
            assert_case(str(tested_rook_attack_mask), str(calculated_rook_attack_count), index + 1))
    return UTestDataModel(test_case_title='Rook Attacks exc. ends Generated Tests', test_cases=unit_tests)


def rook_attack_inc_ends_generation_tests() -> UTestDataModel:
    unit_tests: List[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_rook_attack_count = get_binary(get_rook_attack_mask_inc_end_blockers(position, 0))
        tested_rook_attack_mask = flatten_position(rook_attacks_inc_ends[position.name])
        unit_tests.append(
            assert_case(str(tested_rook_attack_mask), str(calculated_rook_attack_count), index + 1))
    return UTestDataModel(test_case_title='Rook Attacks inc. (no blockers) ends Generation Tests',
                          test_cases=unit_tests)


def rook_attacks_table_test() -> UTestDataModel:
    init_slider_attacks(bishop=False)
    unit_tests: List[UnitTest] = []
    index = 0
    for position in list(Positions)[:-1]:
        for blocker in range(4096):
            calculated_rook_attack = count_set_bits(get_rook_attacks(position.value, blocker) & blocker) in [0, 1,
                                                                                                             2, 3,
                                                                                                             4]
            unit_tests.append(
                assert_case(str(True), str(calculated_rook_attack), index + 1))
            index += 1
    return UTestDataModel(test_case_title='Rook Attacks Generated Tests',
                          test_cases=unit_tests)
