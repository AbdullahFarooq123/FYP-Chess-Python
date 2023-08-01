from typing import List

from ChessEngine.UnitTests.TestData.PawnTestData import pawn_attacks
from ChessEngine.src.Helpers.BeautifyHelpers.GameBeautifyHelpers import get_binary
from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Enums.PlayerSideEnum import PlayerSide

from ChessEngine.src.Helpers.PreCalculationHelpers.PawnPreCalHelpers import get_pawn_attack
from ChessEngine.src.Root.PreCalculationsData import pawn_attack_maps
from ChessEngine.UnitTests.Helpers.UnitTestHelpers import flatten_position, assert_case
from ChessEngine.UnitTests.Models.UnitTestDataModel import UTestDataModel
from ChessEngine.UnitTests.Models.UnitTestModel import UnitTest
from ChessEngine.UnitTests.Models.UnitTestSectionModel import UTestSectionModel


def run_pawn_tests() -> UTestSectionModel:
    attacks_generation_model = pawn_attacks_generation_test()
    attacks_generated_model = pawn_attacks_generated_test()
    return UTestSectionModel('Pawn Tests', [attacks_generation_model, attacks_generated_model])


def pawn_attacks_generation_test() -> UTestDataModel:
    unit_tests: List[UnitTest] = []
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
    unit_tests: List[UnitTest] = []
    case_id = 0
    for player_side in list(PlayerSide)[:-1]:
        for position in list(Positions)[:-1]:
            calculated_pawn_attack_mask = get_binary(pawn_attack_maps[player_side.value][position.value])
            tested_pawn_attack_mask = flatten_position(pawn_attacks[player_side.name][position.name])
            unit_tests.append(
                assert_case(tested_pawn_attack_mask, calculated_pawn_attack_mask, case_id + 1))
            case_id += 1
    return UTestDataModel(test_case_title='Pawn Attacks Generation Tests', test_cases=unit_tests)
