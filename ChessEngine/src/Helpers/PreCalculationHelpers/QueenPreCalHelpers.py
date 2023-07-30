from ChessEngine.src.Helpers.PreCalculationHelpers.BishopPreCalHelpers import get_bishop_attacks
from ChessEngine.src.Helpers.PreCalculationHelpers.RookPreCalHelpers import get_rook_attacks


def get_queen_attacks(position: int, occupancy: int) -> int:
    return get_rook_attacks(position, occupancy) | get_bishop_attacks(position, occupancy)