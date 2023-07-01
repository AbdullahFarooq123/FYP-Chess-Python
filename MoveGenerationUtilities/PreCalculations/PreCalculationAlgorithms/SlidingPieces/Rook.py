from ctypes import c_uint64, c_uint32

from DebugUtilities.GameDependency.BoardDependency.DirectionalDependency.SpecificDirectionDependency import \
    SpecificDirections
from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from MoveGenerationUtilities.Const import right_edge, left_edge, top_edge, bottom_edge
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.PreCalculationDependencies import setOccupancy
from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import count_set_bits, bitmask, move_bit, \
    unsigned
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import rook_attack_count, rook_magic_number, \
    rook_attacks, rook_attacks_table, square_bitmask


def init_rook_attack_mask():
    init_rook_attack_count()


def init_rook_attack_count():
    for position in list(Positions)[:-1]:
        rook_attack_count[position.value] = count_set_bits(get_rook_attack_mask_exc_ends(position))


def get_rook_attack_mask_exc_ends(piece_position: Positions):
    attack_mask = 0
    # Directions are
    # NORTH = 0
    # EAST = 1
    # SOUTH = 2
    # WEST = 3
    directions = list(SpecificDirections)[:4]
    piece_position = bitmask(piece_position.value)
    for direction in directions:
        attack_bit = move_bit(piece_position, direction)
        while attack_bit:
            if direction is SpecificDirections.EAST and attack_bit & right_edge:
                break
            elif direction is SpecificDirections.WEST and attack_bit & left_edge:
                break
            elif direction is SpecificDirections.NORTH and attack_bit & top_edge:
                break
            elif direction is SpecificDirections.SOUTH and attack_bit & bottom_edge:
                break
            attack_mask |= attack_bit
            attack_bit = move_bit(attack_bit, direction)
    return unsigned(attack_mask)


def get_rook_attack_mask_inc_end_blockers(piece_position: Positions, blockers_board: int):
    attack_mask = 0
    # Directions are
    # NORTH = 0
    # EAST = 1
    # SOUTH = 2
    # WEST = 3
    directions = list(SpecificDirections)[:4]
    piece_position = bitmask(piece_position.value)
    for direction in directions:
        attack_bit = move_bit(piece_position, direction)
        while attack_bit:
            attack_mask |= attack_bit
            if blockers_board & attack_bit:
                break
            attack_bit = move_bit(attack_bit, direction)
    return unsigned(attack_mask)


def get_rook_attacks(position: int, occupancy: int) -> int:
    occupancy = c_uint64(occupancy).value
    occupancy = c_uint64(c_uint64(rook_attacks[position]).value & occupancy).value
    occupancy = c_uint64(c_uint64(rook_magic_number[position]).value * occupancy).value
    occupancy = c_uint64(c_uint64(occupancy).value >> (64 - rook_attack_count[position])).value
    return unsigned(rook_attacks_table[position][occupancy])


def get_rook_magic_index_and_attack(position: Positions) -> [int, int]:
    attack_mask = rook_attacks[position.value]
    relevant_bits = count_set_bits(attack_mask)
    occupancy_indices = square_bitmask[relevant_bits]
    for index in range(occupancy_indices):
        occupancy = setOccupancy(index, relevant_bits, attack_mask)
        magic_index = c_uint32(c_uint64(occupancy * rook_magic_number[position.value]).value >> (
                64 - rook_attack_count[position.value])).value
        yield magic_index, get_rook_attack_mask_inc_end_blockers(
            position, occupancy)
