from DebugUtilities.BeautifyDependency.GameBeautify import get_binary, print_bitboard
from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Bishop import get_bishop_attacks
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Rook import \
    get_rook_attack_mask_exc_ends, get_rook_attack_mask_inc_end_blockers, get_rook_attacks
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.SliderAttacks import \
    init_slider_attacks
from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import count_set_bits
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import rook_attacks, rook_attack_count, \
    rook_attacks_table
from UnitTests.UnitTestDependencies import assert_case, flatten_position
from UnitTests.UnitTestModels.UnitTestDataModel import UTestDataModel
from UnitTests.UnitTestModels.UnitTestModel import UnitTest
from UnitTests.UnitTestModels.UnitTestSectionModel import UTestSectionModel
from UnitTests.PreCalculationAlgorithmsTests.SlidingPieces.Rooks.TestedData import *


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
    unit_tests: list[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_rook_attack_count = count_set_bits(get_rook_attack_mask_exc_ends(position))
        tested_rook_attack_mask = tested_rook_attack_counts[position.value]
        unit_tests.append(
            assert_case(str(tested_rook_attack_mask), str(calculated_rook_attack_count), index + 1))
    return UTestDataModel(test_case_title='Rook Attacks Count Generation Tests', test_cases=unit_tests)


def rook_attack_count_generated_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_rook_attack_count = rook_attack_count[position.value]
        tested_rook_attack_mask = tested_rook_attack_counts[position.value]
        unit_tests.append(
            assert_case(str(tested_rook_attack_mask), str(calculated_rook_attack_count), index + 1))
    return UTestDataModel(test_case_title='Rook Attacks Count Generated Tests', test_cases=unit_tests)


def rook_attack_exc_ends_generation_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_rook_attack_count = get_binary(get_rook_attack_mask_exc_ends(position))
        tested_rook_attack_mask = flatten_position(tested_rook_attacks_exc_ends[position.name])
        unit_tests.append(
            assert_case(str(tested_rook_attack_mask), str(calculated_rook_attack_count), index + 1))
    return UTestDataModel(test_case_title='Rook Attacks exc. ends Generation Tests', test_cases=unit_tests)


def rook_attack_exc_ends_generated_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_rook_attack_count = get_binary(rook_attacks[position.value])
        tested_rook_attack_mask = flatten_position(tested_rook_attacks_exc_ends[position.name])
        unit_tests.append(
            assert_case(str(tested_rook_attack_mask), str(calculated_rook_attack_count), index + 1))
    return UTestDataModel(test_case_title='Rook Attacks exc. ends Generated Tests', test_cases=unit_tests)


def rook_attack_inc_ends_generation_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_rook_attack_count = get_binary(get_rook_attack_mask_inc_end_blockers(position, 0))
        tested_rook_attack_mask = flatten_position(tested_rook_attacks_inc_ends[position.name])
        unit_tests.append(
            assert_case(str(tested_rook_attack_mask), str(calculated_rook_attack_count), index + 1))
    return UTestDataModel(test_case_title='Rook Attacks inc. (no blockers) ends Generation Tests',
                          test_cases=unit_tests)


def rook_attacks_table_test() -> UTestDataModel:
    init_slider_attacks(bishop=False)
    unit_tests: list[UnitTest] = []
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
