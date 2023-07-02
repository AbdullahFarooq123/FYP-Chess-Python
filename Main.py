from Migrations.RunMigrations import Migrations

from MoveGenerationUtilities.PreCalculations.PreCalculationsData import square_bitmask
from UnitTests.UnitTestDependencies import TestsOf
from UnitTests.UnitTestEngine import UnitTestEngine
from DebugUtilities.BeautifyDependency.GameBeautify import print_bitboard
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
    # init_attacks()
    position = Positions.e4
    occupancy = square_bitmask[Positions.g3.value]
    attack = get_bishop_attack_mask_inc_end_blockers(piece_position=position, blockers_board=occupancy)
    print_bitboard(attack)


# run_testing()
# run_unit_test()
run_migrations()
