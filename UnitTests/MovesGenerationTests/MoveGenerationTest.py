from UnitTests.MovesGenerationTests.NormalPieces.King.KingCastleMovesTest import run_king_moves_tests
from UnitTests.MovesGenerationTests.NormalPieces.Pawn.PawnMovesTests import run_pawn_moves_tests
from UnitTests.UnitTestModels.UnitTestSectionModel import UTestSectionModel


def run_tests() -> list[UTestSectionModel]:
    return [
        run_pawn_moves_tests(),
        run_king_moves_tests()
    ]
