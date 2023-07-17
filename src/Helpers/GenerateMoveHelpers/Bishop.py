from src.Enums.PositionsEnum import Positions
from src.Enums.PieceNameEnum import PieceName
from src.Enums.PlayerSideEnum import PlayerSide
from src.Helpers.MoveEncryptionHelpers.EncodeMoveHelpers import encode_move
from src.Helpers.MoveGenerationHelpers.OpponentMoveHelpers import \
    is_sliding_piece
from src.Models.GameStateModel import GameState
from src.Helpers.PreCalculationHelpers.BishopPreCalHelpers import get_bishop_attacks
from src.Helpers.PreCalculationHelpers.BitManipulationHelpers import get_least_bit_index, unsigned
from src.Root.PreCalculationsData import square_bitmask


def get_bishop_moves(move_model: GameState) -> list[int]:
    bishop: int = (move_model.fen.white_pieces if move_model.player_attr.player_side == PlayerSide.WHITE else
                   move_model.fen.black_pieces)[PieceName.BISHOP.value]
    bishop_moves: list[int] = []
    while bishop:
        bishop_position: Positions = Positions(get_least_bit_index(bishop))
        bishop_mask = square_bitmask[bishop_position.value]
        is_pinned: bool = bool(bishop_mask & move_model.pinned_pieces.pinned_pieces)
        bishop_attack: int = get_bishop_attacks(position=bishop_position.value, occupancy=move_model.fen.game_board)
        bishop_attack &= unsigned(~move_model.player_attr.player_state)
        if move_model.attack_on_king_attr.check_count == 1:
            if is_sliding_piece(move_model.attack_on_king_attr.attackers[0][1]):
                bishop_attack &= move_model.attack_on_king_attr.attackers_ray
            else:
                bishop_attack &= move_model.attack_on_king_attr.attackers_bitmask
        if is_pinned:
            bishop_attack &= move_model.pinned_pieces.attackers_ray

        while bishop_attack:
            target_square: Positions = Positions(get_least_bit_index(bishop_attack))
            capture_flag: bool = bool(square_bitmask[target_square.value] & move_model.player_attr.opponent_state)
            bishop_moves.append(
                encode_move(source_square=bishop_position,
                            target_square=target_square,
                            piece_name=PieceName.BISHOP,
                            promotion_piece_name=PieceName.NONE,
                            capture_flag=capture_flag,
                            double_push_flag=False,
                            enpassant_flag=False,
                            castle_flag=False))
            bishop_attack &= bishop_attack - 1
        bishop &= bishop - 1
    return bishop_moves
