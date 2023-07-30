from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Root.PreCalculationsData import square_bitmask


class PinnedPiece:
    def __init__(self):
        self.pinned_pieces: int = 0
        self.attackers_ray: int = 0

    def add_piece(self, pinned_piece_position: Positions, attacker_ray: int):
        self.pinned_pieces |= square_bitmask[pinned_piece_position.value]
        self.attackers_ray |= attacker_ray
