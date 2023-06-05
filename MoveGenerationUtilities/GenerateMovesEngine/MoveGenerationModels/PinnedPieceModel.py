from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from DebugUtilities.GameDependency.PieceDependency.PieceNameDependency import PieceName
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import square_bitmask


class PinnedPiece:
    def __init__(self):
        self.pinned_pieces: int = 0
        self.attacker_rays: int = 0

    def add_piece(self, pinned_piece_position: Positions, attacker_ray: int):
        self.pinned_pieces |= square_bitmask[pinned_piece_position.value]
        self.attacker_rays |= attacker_ray
