from ChessEngine.src.Helpers.BeautifyHelpers.GameBeautifyHelpers import get_binary
from ChessEngine.src.Enums.DirectionsEnum import \
    Direction
from ChessEngine.src.Enums.PositionsEnum import Positions

from ChessEngine.src.Helpers.PreCalculationHelpers.DirectionalRayHelpers import \
    get_ray_wrt_pos_dir
from ChessEngine.src.Root.PreCalculationsData import directional_rays
from ChessEngine.UnitTests.TestData.DirectionalRayTestData import *
from ChessEngine.UnitTests.Helpers.UnitTestHelpers import assert_case, flatten_position
from ChessEngine.UnitTests.Models.UnitTestDataModel import UTestDataModel
from ChessEngine.UnitTests.Models.UnitTestModel import UnitTest
from ChessEngine.UnitTests.Models.UnitTestSectionModel import UTestSectionModel


def run_directional_rays_tests() -> UTestSectionModel:
    rays_generation_tests = directional_rays_generation_tests()
    rays_generated_tests = directional_rays_generated_tests()
    return UTestSectionModel('Directional Rays Tests',
                             [rays_generation_tests, rays_generated_tests])


def directional_rays_generation_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    index = 0
    for direction in list(Direction)[:8]:
        for position in list(Positions)[:-1]:
            calculated_ray = get_binary(get_ray_wrt_pos_dir(direction, position))
            tested_ray = flatten_position(tested_directional_rays[direction.name][position.name])
            unit_tests.append(
                assert_case(tested_ray, calculated_ray, index + 1))
            index += 1
    return UTestDataModel(test_case_title='Directional Rays Generation Tests', test_cases=unit_tests)


def directional_rays_generated_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    index = 0
    for direction in list(Direction)[:8]:
        for position in list(Positions)[:-1]:
            calculated_ray = get_binary(directional_rays[direction.value][position.value])
            tested_ray = flatten_position(tested_directional_rays[direction.name][position.name])
            unit_tests.append(
                assert_case(tested_ray, calculated_ray, index + 1))
            index += 1
    return UTestDataModel(test_case_title='Directional Rays Generated Tests', test_cases=unit_tests)


