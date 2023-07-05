from DebugUtilities.GameDependency.PieceDependency.PieceNameDependency import PieceName
from FenUtilities.FenDecrypt import decrypt_fen
from FenUtilities.FenModel import Fen
from MoveGenerationUtilities.GenerateMovesEngine.MoveGenerationDependencies.GetAttackersDependencies import \
    get_alignment_wrt_each_other
from MoveGenerationUtilities.Migrations.RunMigrations import Migrations
from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import get_least_bit_index

from MoveGenerationUtilities.PreCalculations.PreCalculationsData import square_bitmask
from UnitTests.UnitTestDependencies import TestsOf
from UnitTests.UnitTestEngine import UnitTestEngine
from DebugUtilities.BeautifyDependency.GameBeautify import print_bitboard, get_binary
from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Bishop import \
    get_bishop_attack_mask_inc_end_blockers


def run_unit_test():
    u_engine = UnitTestEngine(show_only_tests=TestsOf.FAILED, print_test_cases=TestsOf.FAILED,
                              print_test_case_details=TestsOf.FAILED)
    u_engine.run_tests()
    u_engine.print_tests()


def run_migrations():
    Migrations().run_migrations()


def run_testing():
    mask = square_bitmask[Positions.e4.value]
    print_bitboard(mask)
    print_bitboard(mask<<8)


if __name__ == '__main__':
    run_testing()
    # run_unit_test()
    # run_migrations()
