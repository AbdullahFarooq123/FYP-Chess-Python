from ChessEngine.src.Enums.DirectionsEnum import \
    Direction
from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Helpers.PreCalculationHelpers.BitManipulationHelpers import bitmask, unsigned, \
    move_bit_by_direction


def init_king_attacks():
    king_attack_maps = [0 for _ in list(Positions)[:-1]]
    for position in list(Positions)[:-1]:
        king_attack_maps[position.value] = get_king_attack(position.value)
    return king_attack_maps, 'king_attack_maps'


def get_king_attack(position: int) -> int:
    attacks = 0
    piece_position = bitmask(position)
    # directions are
    # NORTH = 0
    # EAST = 1
    # SOUTH = 2
    # WEST = 3
    # NORTH_EAST = 4
    # NORTH_WEST = 5
    # SOUTH_EAST = 6
    # SOUTH_WEST = 7
    directions = list(Direction)[:8]
    for direction in directions:
        attacks |= move_bit_by_direction(piece_position, direction)
    return unsigned(attacks)
