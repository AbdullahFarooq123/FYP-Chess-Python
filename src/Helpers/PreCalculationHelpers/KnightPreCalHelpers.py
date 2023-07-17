from src.Enums.DirectionsEnum import \
    Direction
from src.Enums.PositionsEnum import Positions
from src.Helpers.PreCalculationHelpers.BitManipulationHelpers import bitmask, move_bit_by_position, unsigned


def init_knight_attacks():
    knight_attack_maps = [0 for _ in list(Positions)[:-1]]
    for position in list(Positions)[:-1]:
        knight_attack_maps[position.value] = get_knight_attack(position.value)
    return knight_attack_maps, 'knight_attack_maps'


def get_knight_attack(position: int) -> int:
    attacks = 0
    piece_position = bitmask(position)
    # Directions are
    # NORTH_EAST_EAST = 8
    # NORTH_WEST_WEST = 9
    # NORTH_NORTH_EAST = 10
    # NORTH_NORTH_WEST = 11
    # SOUTH_EAST_EAST = 12
    # SOUTH_WEST_WEST = 13
    # SOUTH_SOUTH_EAST = 14
    # SOUTH_SOUTH_WEST = 15
    directions = list(Direction)[8:16]
    for direction in directions:
        attacks |= move_bit_by_position(piece_position, direction)
    return unsigned(attacks)
