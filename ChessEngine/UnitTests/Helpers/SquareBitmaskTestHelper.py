from typing import List

from ChessEngine.src.Helpers.BeautifyHelpers.GameBeautifyHelpers import get_binary
from ChessEngine.src.Enums.PositionsEnum import Positions

from ChessEngine.src.Helpers.PreCalculationHelpers.BitManipulationHelpers import bitmask
from ChessEngine.src.Root.PreCalculationsData import square_bitmask
from ChessEngine.UnitTests.TestData.SquareBitmaskTestData import tested_square_bitmask
from ChessEngine.UnitTests.Helpers.UnitTestHelpers import assert_case, flatten_position
from ChessEngine.UnitTests.Models.UnitTestDataModel import UTestDataModel
from ChessEngine.UnitTests.Models.UnitTestModel import UnitTest
from ChessEngine.UnitTests.Models.UnitTestSectionModel import UTestSectionModel


def run_square_bitmask_tests() -> UTestSectionModel:
    mask_generation_model = square_bitmask_generation_tests()
    mask_generated_model = square_bitmask_generated_tests()
    return UTestSectionModel('Bitmask Tests', [mask_generation_model, mask_generated_model])


def square_bitmask_generation_tests() -> UTestDataModel:
    unit_tests: List[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_bitmask = get_binary(bitmask(position.value))
        tested_bitmask = flatten_position(tested_square_bitmask[position.name])
        unit_tests.append(
            assert_case(tested_bitmask, calculated_bitmask, index + 1))
    return UTestDataModel(test_case_title='Bitmask Generation Tests', test_cases=unit_tests)


def square_bitmask_generated_tests() -> UTestDataModel:
    unit_tests: List[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_bitmask = get_binary(square_bitmask[position.value])
        tested_bitmask = flatten_position(tested_square_bitmask[position.name])
        unit_tests.append(
            assert_case(tested_bitmask, calculated_bitmask, index + 1))
    return UTestDataModel(test_case_title='Bitmask Generated Tests', test_cases=unit_tests)
