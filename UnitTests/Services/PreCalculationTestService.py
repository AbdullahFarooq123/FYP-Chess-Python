from UnitTests.Helpers.DirectionalRayTestHelper import run_directional_rays_tests
from UnitTests.Helpers.SquareBitmaskTestHelper import run_square_bitmask_tests
from UnitTests.Models.UnitTestSectionModel import UTestSectionModel
from UnitTests.Helpers.KingMoveGenTestHelper import run_king_tests
from UnitTests.Helpers.KnightMoveGenTestHelper import run_knight_tests
from UnitTests.Helpers.PawnMoveGenTestHelper import run_pawn_tests
from UnitTests.Helpers.BishopMoveGenTestHelper import run_bishop_tests
from UnitTests.Helpers.RookMoveGenTestHelper import run_rook_tests


def run_tests() -> list[UTestSectionModel]:
    return [run_square_bitmask_tests(),
            run_directional_rays_tests(),
            run_king_tests(),
            run_knight_tests(),
            run_pawn_tests(),
            run_bishop_tests(),
            run_rook_tests()]
