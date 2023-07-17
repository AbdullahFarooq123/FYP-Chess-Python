from UnitTests.TestData.PawnTestData import pawn_attacks
from src.Helpers.BeautifyHelpers.GameBeautifyHelpers import get_binary
from src.Enums.PositionsEnum import Positions
from src.Enums.PlayerSideEnum import PlayerSide

from src.Helpers.PreCalculationHelpers.PawnPreCalHelpers import get_pawn_attack
from src.Root.PreCalculationsData import pawn_attack_maps
from UnitTests.Helpers.UnitTestHelpers import flatten_position, assert_case
from UnitTests.Models.UnitTestDataModel import UTestDataModel
from UnitTests.Models.UnitTestModel import UnitTest
from UnitTests.Models.UnitTestSectionModel import UTestSectionModel


def run_pawn_tests() -> UTestSectionModel:
    attacks_generation_model = pawn_attacks_generation_test()
    attacks_generated_model = pawn_attacks_generated_test()
    return UTestSectionModel('Pawn Tests', [attacks_generation_model, attacks_generated_model])


def pawn_attacks_generation_test() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    case_id = 0
    for player_side in list(PlayerSide)[:-1]:
        for position in list(Positions)[:-1]:
            calculated_pawn_attack_mask = get_binary(get_pawn_attack(player_side, position.value))
            tested_pawn_attack_mask = flatten_position(pawn_attacks[player_side.name][position.name])
            unit_tests.append(
                assert_case(tested_pawn_attack_mask, calculated_pawn_attack_mask, case_id + 1))
            case_id += 1
    return UTestDataModel(test_case_title='Pawn Attacks Generation Tests', test_cases=unit_tests)


def pawn_attacks_generated_test() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    case_id = 0
    for player_side in list(PlayerSide)[:-1]:
        for position in list(Positions)[:-1]:
            calculated_pawn_attack_mask = get_binary(pawn_attack_maps[player_side.value][position.value])
            tested_pawn_attack_mask = flatten_position(pawn_attacks[player_side.name][position.name])
            unit_tests.append(
                assert_case(tested_pawn_attack_mask, calculated_pawn_attack_mask, case_id + 1))
            case_id += 1
    return UTestDataModel(test_case_title='Pawn Attacks Generation Tests', test_cases=unit_tests)
