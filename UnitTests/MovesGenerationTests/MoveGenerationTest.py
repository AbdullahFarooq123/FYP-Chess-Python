from UnitTests.MovesGenerationTests.NormalPieces.King.KingMovesTest import run_king_moves_tests
from UnitTests.MovesGenerationTests.NormalPieces.Knight.KnightMovesTest import run_knight_moves_tests
from UnitTests.MovesGenerationTests.NormalPieces.Pawn.PawnMovesTests import run_pawn_moves_tests
from UnitTests.MovesGenerationTests.SlidingPieces.Bishop.BishopMovesTests import run_bishop_moves_tests
from UnitTests.MovesGenerationTests.SlidingPieces.Queen.QueenMovesTests import run_queen_moves_tests
from UnitTests.MovesGenerationTests.SlidingPieces.Rook.RookMovesTests import run_rook_moves_tests
from UnitTests.UnitTestModels.UnitTestSectionModel import UTestSectionModel


def run_tests() -> list[UTestSectionModel]:
    return [
        run_pawn_moves_tests(),
        run_king_moves_tests(),
        run_knight_moves_tests(),
        run_rook_moves_tests(),
        run_bishop_moves_tests(),
        run_queen_moves_tests()
    ]
