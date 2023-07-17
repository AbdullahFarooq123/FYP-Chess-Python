from src.Helpers.PreCalculationHelpers.BitManipulationHelpers import get_least_bit_index
from src.Root.PreCalculationsData import square_bitmask


def set_occupancy(index: int, attacks_count: int, piece_attack_map: int) -> int:
    occupancy = 0
    for i in range(attacks_count):
        bit_index = get_least_bit_index(piece_attack_map)
        piece_attack_map &= piece_attack_map - 1
        if index & square_bitmask[i]:
            occupancy |= square_bitmask[bit_index]
    return occupancy
