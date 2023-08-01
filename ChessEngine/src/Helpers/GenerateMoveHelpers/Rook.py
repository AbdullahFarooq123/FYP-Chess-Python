from typing import List

from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Enums.PieceNameEnum import PieceName
from ChessEngine.src.Enums.PlayerSideEnum import PlayerSide
from ChessEngine.src.Helpers.MoveEncryptionHelpers.EncodeMoveHelpers import encode_move
from ChessEngine.src.Helpers.MoveGenerationHelpers.OpponentMoveHelpers import \
    is_sliding_piece
from ChessEngine.src.Models.GameStateModel import GameState
from ChessEngine.src.Helpers.PreCalculationHelpers.RookPreCalHelpers import get_rook_attacks
from ChessEngine.src.Helpers.PreCalculationHelpers.BitManipulationHelpers import get_least_bit_index, unsigned
from ChessEngine.src.Root.PreCalculationsData import square_bitmask


def get_rook_moves(move_model: GameState) -> List[int]:
    rook: int = (move_model.fen.white_pieces if move_model.player_attr.player_side == PlayerSide.WHITE else
                 move_model.fen.black_pieces)[PieceName.ROOK.value]
    rook_moves: List[int] = []
    while rook:
        rook_position: Positions = Positions(get_least_bit_index(rook))
        rook_mask = square_bitmask[rook_position.value]
        is_pinned: bool = bool(rook_mask & move_model.pinned_pieces.pinned_pieces)
        rook_attack: int = get_rook_attacks(position=rook_position.value, occupancy=move_model.fen.game_board)
        rook_attack &= unsigned(~move_model.player_attr.player_state)
        if move_model.attack_on_king_attr.check_count == 1:
            if is_sliding_piece(move_model.attack_on_king_attr.attackers[0][1]):
                rook_attack &= move_model.attack_on_king_attr.attackers_ray
            else:
                rook_attack &= move_model.attack_on_king_attr.attackers_bitmask
        if is_pinned:
            rook_attack &= move_model.pinned_pieces.attackers_ray

        while rook_attack:
            target_square: Positions = Positions(get_least_bit_index(rook_attack))
            capture_flag: bool = bool(square_bitmask[target_square.value] & move_model.player_attr.opponent_state)
            rook_moves.append(
                encode_move(source_square=rook_position,
                            target_square=target_square,
                            piece_name=PieceName.ROOK,
                            promotion_piece_name=PieceName.NONE,
                            capture_flag=capture_flag,
                            double_push_flag=False,
                            enpassant_flag=False,
                            castle_flag=False))
            rook_attack &= rook_attack - 1
        rook &= rook - 1
    return rook_moves
