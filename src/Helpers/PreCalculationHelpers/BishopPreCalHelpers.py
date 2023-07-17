from ctypes import c_uint64, c_uint32

from src.Enums.DirectionsEnum import \
    Direction
from src.Enums.PositionsEnum import Positions
from src.Helpers.PreCalculationHelpers.BitManipulationHelpers import count_set_bits, bitmask, move_bit_by_position, \
    unsigned









from src.Helpers.PreCalculationHelpers.SetOccupancyHelpers import set_occupancy
from src.Root.Const import right_edge, left_edge, top_edge, bottom_edge
from src.Root.PreCalculationsData import bishop_attack_count, bishop_magic_number, \
    bishop_attacks, bishop_attacks_table, square_bitmask


def init_bishop_attack_count():
    bishop_attack_count = [0 for _ in Positions]
    for position in Positions:
        bishop_attack_count[position.value] = count_set_bits(get_bishop_attack_mask_exc_ends(position))
    return bishop_attack_count, 'bishop_attack_count'


def init_bishop_attack_mask_exc_ends():
    bishop_attacks = [0 for _ in Positions]
    for position in Positions:
        bishop_attacks[position.value] = get_bishop_attack_mask_exc_ends(position)
    return bishop_attacks, 'bishop_attacks'


def get_bishop_attack_mask_exc_ends(piece_position: Positions):
    attack_mask = 0
    # Directions are
    # NORTH_EAST = 4
    # NORTH_WEST = 5
    # SOUTH_EAST = 6
    # SOUTH_WEST = 7
    directions = list(Direction)[4:8]
    piece_position = bitmask(piece_position.value)
    for direction in directions:
        attack_bit = move_bit_by_position(piece_position, direction)
        while attack_bit:
            if direction is Direction.NORTH_EAST and attack_bit & (right_edge | top_edge):
                break
            elif direction is Direction.NORTH_WEST and attack_bit & (left_edge | top_edge):
                break
            elif direction is Direction.SOUTH_EAST and attack_bit & (right_edge | bottom_edge):
                break
            elif direction is Direction.SOUTH_WEST and attack_bit & (left_edge | bottom_edge):
                break
            attack_mask |= attack_bit
            attack_bit = move_bit_by_position(attack_bit, direction)
    return unsigned(attack_mask)


def get_bishop_attack_mask_inc_end_blockers(piece_position: Positions, blockers_board: int):
    attack_mask = 0
    # Directions are
    # NORTH_EAST = 4
    # NORTH_WEST = 5
    # SOUTH_EAST = 6
    # SOUTH_WEST = 7
    directions = list(Direction)[4:8]
    piece_position = bitmask(piece_position.value)
    for direction in directions:
        attack_bit = move_bit_by_position(piece_position, direction)
        while attack_bit:
            # print_bitboard(attack_bit)
            attack_mask |= attack_bit
            if blockers_board & attack_bit:
                break
            attack_bit = move_bit_by_position(attack_bit, direction)
    return unsigned(attack_mask)


def get_bishop_attacks(position: int, occupancy: int):
    magic_index = get_bishop_magic_index(position, occupancy)
    attack = bishop_attacks_table[position][magic_index]
    return unsigned(attack)


def get_bishop_magic_index(position: int, occupancy: int) -> int:
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
        occupancy = set_occupancy(index, relevant_bits, attack_mask)
        magic_index = c_uint32(c_uint64(occupancy * bishop_magic_number[position.value]).value >> (
                64 - bishop_attack_count[position.value])).value
        yield magic_index, get_bishop_attack_mask_inc_end_blockers(
            position, occupancy)
