import json
import sqlite3
from sqlite3 import Cursor

from DebugUtilities.GameDependency.BoardDependency.DirectionalDependency.SpecificDirectionDependency import \
    SpecificDirections
from DebugUtilities.GameDependency.PieceDependency.PieceNameDependency import PieceName
from FenUtilities.FenDecrypt import *
from Migrations.Models.BishopAttacksTableModel import BishopAttacksTableModelClass
from Migrations.RunMigrations import Migrations
from MoveGenerationUtilities.Const import white_king_side_castle_occupancy, white_queen_side_castle_occupancy, \
    black_king_side_castle_occupancy, black_queen_side_castle_occupancy

from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.SliderAttacks import \
    init_slider_attacks
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SquareBitmaskDependencies import init_squares
from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import count_set_bits, move_bit, bitmask
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import square_bitmask, king_attack_maps
from MoveGenerationUtilities.PreCalculations.PreCalculationsInit import init_attacks
from UnitTests.UnitTestDependencies import TestsOf
from UnitTests.UnitTestEngine import UnitTestEngine
from DebugUtilities.BeautifyDependency.GameBeautify import print_bitboard, get_binary, print_fen_board, print_game_board
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Rook import \
    get_rook_attack_mask_inc_end_blockers, get_rook_attacks
from DebugUtilities.BeautifyDependency.GameBeautify import print_attack_map
from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Bishop import \
    get_bishop_attack_mask_inc_end_blockers, get_bishop_attacks, get_bishop_occupancy


def run_unit_test():
    u_engine = UnitTestEngine(show_only_tests=TestsOf.FAILED, print_test_cases=TestsOf.FAILED,
                              print_test_case_details=TestsOf.FAILED)
    u_engine.run_tests()
    u_engine.print_tests()


def run_migrations():
    Migrations().run_migrations()


def run_testing():
    connection = sqlite3.connect('ChessDb')
    cursor: Cursor = connection.cursor()
    val = BishopAttacksTableModelClass(cursor)
    position = Positions.a8
    occupancy = 0
    occupancy = get_bishop_occupancy(position.value,occupancy)
    val = val.run_select_one(select_col=f'{BishopAttacksTableModelClass.Columns.Value.value}', where_clause=f'WHERE {BishopAttacksTableModelClass.Columns.Position.value} = "{position.name}" AND {BishopAttacksTableModelClass.Columns.MagicIndex.value} = {occupancy}')
    print(val)

# run_testing()
# run_migrations()
run_unit_test()