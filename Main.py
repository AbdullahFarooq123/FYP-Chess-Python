import json

from DebugUtilities.GameDependency.BoardDependency.DirectionalDependency.SpecificDirectionDependency import \
    SpecificDirections
from FenUtilities.FenDecrypt import *

from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.SliderAttacks import \
    init_slider_attacks
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SquareBitmaskDependencies import init_squares
from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import count_set_bits, move_bit
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import square_bitmask, king_attack_maps
from UnitTests.UnitTestDependencies import TestsOf
from UnitTests.UnitTestEngine import UnitTestEngine
from DebugUtilities.BeautifyDependency.GameBeautify import print_bitboard, get_binary, print_fen_board
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Rook import \
    get_rook_attack_mask_inc_end_blockers
from DebugUtilities.BeautifyDependency.GameBeautify import print_attack_map
from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Bishop import \
    get_bishop_attack_mask_inc_end_blockers, get_bishop_attacks


def run_main():
    u_engine = UnitTestEngine(show_only_tests=TestsOf.FAILED, print_test_cases=TestsOf.FAILED,
                              print_test_case_details=TestsOf.FAILED)
    u_engine.run_tests()
    u_engine.print_tests()


def run_testing():
    fen: Fen = decryptFen('3k4/8/3r4/3Pp3/8/8/8/3K4 w - e6 0 3')
    print_fen_board('3k4/8/3r4/3Pp3/8/8/8/3K4 w - e6 0 3')
    print_bitboard(fen.game_board & fen.white_board)
    print(get_binary(fen.game_board))
    print(fen.game_board)


# run_testing()
run_main()
