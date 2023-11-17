from ChessEngine.UnitTests.Services.KingMoveTestService import run_king_moves_tests
from ChessEngine.UnitTests.Helpers.KnightMoveTestHelper import run_knight_moves_tests
from ChessEngine.UnitTests.Helpers.PawnMovesTestHelper import run_pawn_moves_tests
from ChessEngine.UnitTests.Helpers.BishopMoveTestHelper import run_bishop_moves_tests
from ChessEngine.UnitTests.Helpers.QueenMoveTestHelper import run_queen_moves_tests
from ChessEngine.UnitTests.Helpers.RookMoveTestHelper import run_rook_moves_tests
from ChessEngine.UnitTests.Models.UnitTestSectionModel import UTestSectionModel


def run_tests() -> list[UTestSectionModel]:
    return [
        run_pawn_moves_tests(),
        run_king_moves_tests(),
        run_knight_moves_tests(),
        run_rook_moves_tests(),
        run_bishop_moves_tests(),
        run_queen_moves_tests()
    ]
