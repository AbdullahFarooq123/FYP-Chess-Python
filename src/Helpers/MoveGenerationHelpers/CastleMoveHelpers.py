from src.Enums.PieceNameEnum import PieceName
from src.Enums.PlayerSideEnum import PlayerSide
from src.Enums.PositionsEnum import Positions
from src.Helpers.PreCalculationHelpers.BishopPreCalHelpers import get_bishop_attacks
from src.Helpers.PreCalculationHelpers.RookPreCalHelpers import get_rook_attacks
from src.Helpers.PreCalculationHelpers.BitManipulationHelpers import get_least_bit_index
from src.Root.PreCalculationsData import pawn_attack_maps, knight_attack_maps, \
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
        squares &= squares - 1
    return False


def squares_are_occupied(squares: int, board_state: int) -> bool:
    return bool(squares & board_state)
