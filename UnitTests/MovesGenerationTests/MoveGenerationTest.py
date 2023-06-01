from UnitTests.MovesGenerationTests.NormalPieces.Pawn.PawnMovesTests import run_pawn_moves_tests
from UnitTests.UnitTestModels.UnitTestSectionModel import UTestSectionModel


def run_tests() -> list[UTestSectionModel]:
    return [
        run_pawn_moves_tests()
    ]
