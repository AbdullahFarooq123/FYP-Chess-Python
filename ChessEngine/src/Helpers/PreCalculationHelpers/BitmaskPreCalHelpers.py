from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Helpers.PreCalculationHelpers.BitManipulationHelpers import bitmask


def init_squares() -> [list[int], str]:
    square_bitmask = [0 for _ in list(Positions)[:-1]]
    for position in list(Positions)[:-1]:
        square_bitmask[position.value] = (bitmask(position.value))
    return square_bitmask, 'square_bitmask'
