from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from DebugUtilities.GameDependency.PieceDependency.PieceNameDependency import PieceName
from DebugUtilities.GameDependency.PlayerDependency.PlayerSideDependency import PlayerSide
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Bishop import get_bishop_attacks
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Rook import get_rook_attacks
from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import get_least_bit_index
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import pawn_attack_maps, knight_attack_maps, \
    king_attack_maps


def squares_are_attacked(squares: int, opponent_pieces: list[int], side: PlayerSide, board_state: int) -> bool:
    while squares:
        position: Positions = Positions(get_least_bit_index(squares))
        pawn_attack: int = pawn_attack_maps[side.value][position.value]
        rook_attacks: int = get_rook_attacks(position=position.value, occupancy=board_state)
        bishop_attacks: int = get_bishop_attacks(position=position.value, occupancy=board_state)
        queen_attacks: int = rook_attacks | bishop_attacks
        knight_attacks: int = knight_attack_maps[position.value]
        king_attacks: int = king_attack_maps[position.value]
        if pawn_attack & opponent_pieces[PieceName.PAWN.value]:
            return True
        elif rook_attacks & opponent_pieces[PieceName.ROOK.value]:
            return True
        elif bishop_attacks & opponent_pieces[PieceName.BISHOP.value]:
            return True
        elif queen_attacks & opponent_pieces[PieceName.QUEEN.value]:
            return True
        elif knight_attacks & opponent_pieces[PieceName.KNIGHT.value]:
            return True
        elif king_attacks & opponent_pieces[PieceName.KING.value]:
            return True
        squares &= squares-1
    return False
