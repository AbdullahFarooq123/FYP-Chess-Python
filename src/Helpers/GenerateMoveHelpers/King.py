from src.Enums.PositionsEnum import Positions
from src.Enums.PieceNameEnum import PieceName
from src.Enums.PlayerSideEnum import PlayerSide
from src.Helpers.MoveEncryptionHelpers.EncodeMoveHelpers import encode_move
from src.Models.GameStateModel import GameState
from src.Helpers.PreCalculationHelpers.KingPreCalHelpers import get_king_attack
from src.Helpers.PreCalculationHelpers.BitManipulationHelpers import get_least_bit_index, unsigned
from src.Root.PreCalculationsData import square_bitmask


def get_king_moves(move_model: GameState) -> list[int]:
    king: int = (move_model.fen.white_pieces if move_model.player_attr.player_side == PlayerSide.WHITE else
                 move_model.fen.black_pieces)[PieceName.KING.value]
    king_moves: list[int] = []
    while king:
        king_position: Positions = Positions(get_least_bit_index(king))
        king_attack: int = get_king_attack(position=king_position.value)
        king_attack &= unsigned(~move_model.player_attr.player_state)
        king_attack &= ~move_model.attack_on_king_attr.opponent_attacks
        while king_attack:
            target_square: Positions = Positions(get_least_bit_index(king_attack))
            capture_flag: bool = bool(square_bitmask[target_square.value] & move_model.player_attr.opponent_state)
            king_moves.append(
                encode_move(source_square=king_position,
                            target_square=target_square,
                            piece_name=PieceName.KING,
                            promotion_piece_name=PieceName.NONE,
                            capture_flag=capture_flag,
                            double_push_flag=False,
                            enpassant_flag=False,
                            castle_flag=False))
            king_attack &= king_attack - 1
        king &= king - 1
    return king_moves
