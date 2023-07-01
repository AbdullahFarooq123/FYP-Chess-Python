from ctypes import c_uint64, c_uint32

from DebugUtilities.GameDependency.BoardDependency.DirectionalDependency.SpecificDirectionDependency import \
    SpecificDirections
from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from MoveGenerationUtilities.Const import right_edge, left_edge, top_edge, bottom_edge
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.PreCalculationDependencies import setOccupancy
from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import count_set_bits, bitmask, move_bit, \
    unsigned
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import bishop_attack_count, bishop_magic_number, \
    bishop_attacks, bishop_attacks_table, square_bitmask


def init_bishop_attack_mask():
    init_bishop_attack_count()


def init_bishop_attack_count():
    for position in Positions:
        bishop_attack_count[position.value] = count_set_bits(get_bishop_attack_mask_exc_ends(position))


def get_bishop_attack_mask_exc_ends(piece_position: Positions):
    attack_mask = 0
    # Directions are
    # NORTH_EAST = 4
    # NORTH_WEST = 5
    # SOUTH_EAST = 6
    # SOUTH_WEST = 7
    directions = list(SpecificDirections)[4:8]
    piece_position = bitmask(piece_position.value)
    for direction in directions:
        attack_bit = move_bit(piece_position, direction)
        while attack_bit:
            if direction is SpecificDirections.NORTH_EAST and attack_bit & (right_edge | top_edge):
                break
            elif direction is SpecificDirections.NORTH_WEST and attack_bit & (left_edge | top_edge):
                break
            elif direction is SpecificDirections.SOUTH_EAST and attack_bit & (right_edge | bottom_edge):
                break
            elif direction is SpecificDirections.SOUTH_WEST and attack_bit & (left_edge | bottom_edge):
                break
            attack_mask |= attack_bit
            attack_bit = move_bit(attack_bit, direction)
    return unsigned(attack_mask)


def get_bishop_attack_mask_inc_end_blockers(piece_position: Positions, blockers_board: int):
    attack_mask = 0
    # Directions are
    # NORTH_EAST = 4
    # NORTH_WEST = 5
    # SOUTH_EAST = 6
    # SOUTH_WEST = 7
    directions = list(SpecificDirections)[4:8]
    piece_position = bitmask(piece_position.value)
    for direction in directions:
        attack_bit = move_bit(piece_position, direction)
        while attack_bit:
            attack_mask |= attack_bit
            if blockers_board & attack_bit:
                break
            attack_bit = move_bit(attack_bit, direction)
    return unsigned(attack_mask)


def get_bishop_attacks(position: int, occupancy: int):
    occupancy = get_bishop_occupancy(position, occupancy)
    return unsigned(bishop_attacks_table[position][occupancy])


def get_bishop_occupancy(position: int, occupancy: int) -> int:
    occupancy = c_uint64(occupancy).value
    occupancy = c_uint64(c_uint64(bishop_attacks[position]).value & occupancy).value
    occupancy = c_uint64(c_uint64(bishop_magic_number[position]).value * occupancy).value
    occupancy = c_uint64(c_uint64(occupancy).value >> (64 - bishop_attack_count[position])).value
    return occupancy


def get_bishop_magic_index_and_attack(position: Positions) -> [int, int]:
    attack_mask = bishop_attacks[position.value]
    relevant_bits = count_set_bits(attack_mask)
    occupancy_indices = square_bitmask[relevant_bits]
    for index in range(occupancy_indices):
        occupancy = setOccupancy(index, relevant_bits, attack_mask)
        magic_index = c_uint32(c_uint64(occupancy * bishop_magic_number[position.value]).value >> (
                64 - bishop_attack_count[position.value])).value
        yield magic_index, get_bishop_attack_mask_inc_end_blockers(
            position, occupancy)
