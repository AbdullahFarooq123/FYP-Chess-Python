from src.Enums.PositionsEnum import Positions
from src.Enums.PieceNameEnum import PieceName
from src.Enums.PlayerSideEnum import PlayerSide
from src.Helpers.MoveEncryptionHelpers.EncodeMoveHelpers import encode_move
from src.Helpers.MoveGenerationHelpers.OpponentMoveHelpers import \
    is_sliding_piece
from src.Models.GameStateModel import GameState
from src.Helpers.PreCalculationHelpers.KnightPreCalHelpers import get_knight_attack
from src.Helpers.PreCalculationHelpers.BitManipulationHelpers import get_least_bit_index, unsigned
from src.Root.PreCalculationsData import square_bitmask


def get_knight_moves(move_model: GameState) -> list[int]:
    knight: int = (move_model.fen.white_pieces if move_model.player_attr.player_side == PlayerSide.WHITE else
                   move_model.fen.black_pieces)[PieceName.KNIGHT.value]
    knight_moves: list[int] = []
    while knight:
        knight_position: Positions = Positions(get_least_bit_index(knight))
        knight_mask = square_bitmask[knight_position.value]
        is_pinned: bool = bool(knight_mask & move_model.pinned_pieces.pinned_pieces)
        knight_attack: int = get_knight_attack(position=knight_position.value)
        knight_attack &= unsigned(~move_model.player_attr.player_state)
        if move_model.attack_on_king_attr.check_count == 1:
            if is_sliding_piece(move_model.attack_on_king_attr.attackers[0][1]):
                knight_attack &= move_model.attack_on_king_attr.attackers_ray
            else:
                knight_attack &= move_model.attack_on_king_attr.attackers_bitmask
        if is_pinned:
            knight_attack &= move_model.pinned_pieces.attackers_ray

        while knight_attack:
            target_square: Positions = Positions(get_least_bit_index(knight_attack))
            capture_flag: bool = bool(square_bitmask[target_square.value] & move_model.player_attr.opponent_state)
            knight_moves.append(
                encode_move(source_square=knight_position,
                            target_square=target_square,
                            piece_name=PieceName.KNIGHT,
                            promotion_piece_name=PieceName.NONE,
                            capture_flag=capture_flag,
                            double_push_flag=False,
                            enpassant_flag=False,
                            castle_flag=False))
            knight_attack &= knight_attack - 1
        knight &= knight - 1
    return knight_moves
