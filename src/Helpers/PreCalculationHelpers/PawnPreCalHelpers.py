from src.Enums.DirectionsEnum import \
    Direction
from src.Enums.PlayerSideEnum import PlayerSide
from src.Enums.PositionsEnum import Positions
from src.Helpers.PreCalculationHelpers.BitManipulationHelpers import bitmask, move_bit_by_position, unsigned


def init_pawn_attacks():
    pawn_attack_maps = [[0 for _ in list(Positions)[:-1]] for _ in list(PlayerSide)[:-1]]
    for side in list(PlayerSide)[:-1]:
        for position in list(Positions)[:-1]:
            pawn_attack_maps[side.value][position.value] = get_pawn_attack(side, position.value)
    return pawn_attack_maps, 'pawn_attack_maps'


def get_pawn_attack(side: PlayerSide, position: int) -> int:
    attacks = 0
    piece_position = bitmask(position)
    # if black side Directions are
    # SOUTH_EAST = 6
    # SOUTH_WEST = 7
    # else
    # NORTH_EAST = 4
    # NORTH_WEST = 5
    directions = list(Direction)[6:8] \
        if side is PlayerSide.BLACK else \
        list(Direction)[4:6]
    for pos in directions:
        attacks |= move_bit_by_position(piece_position, pos)
    return unsigned(attacks)
