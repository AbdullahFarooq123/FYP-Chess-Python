from typing import List

from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Enums.PieceNameEnum import PieceName
from ChessEngine.src.Enums.PlayerSideEnum import PlayerSide
from ChessEngine.src.Root.Const import white_queen_side_castle_occupancy, white_king_side_castle_occupancy
from ChessEngine.src.Helpers.MoveEncryptionHelpers.EncodeMoveHelpers import encode_move
from ChessEngine.src.Helpers.MoveGenerationHelpers.CastleMoveHelpers import \
    squares_are_attacked, squares_are_occupied
from ChessEngine.src.Models.CastleModel import Castle
from ChessEngine.src.Models.GameStateModel import GameState
from ChessEngine.src.Helpers.PreCalculationHelpers.BitManipulationHelpers import get_least_bit_index


def get_white_castle_moves(move_model: GameState) -> List[int]:
    white_king: int = move_model.fen.white_pieces[PieceName.KING.value]
    white_king_position: Positions = Positions(get_least_bit_index(white_king))
    castle_moves: List[int] = []
    white_castle: Castle = move_model.white_castle
    check_count: int = move_model.attack_on_king_attr.check_count
    board_state: int = move_model.fen.game_board
    if white_castle.can_castle() and check_count == 0:
        if white_castle.can_queen_side_castle() and not squares_are_attacked(
                squares=white_queen_side_castle_occupancy, opponent_pieces=move_model.player_attr.opponent_pieces,
                side=PlayerSide.WHITE, board_state=move_model.fen.game_board) and not squares_are_occupied(
                board_state=board_state, squares=white_queen_side_castle_occupancy):
            castle_moves.append(
                encode_move(source_square=white_king_position,
                            target_square=Positions.c1,
                            piece_name=PieceName.KING,
                            promotion_piece_name=PieceName.NONE,
                            capture_flag=False,
                            double_push_flag=False,
                            enpassant_flag=False,
                            castle_flag=True))
        if move_model.white_castle.can_king_side_castle() and not squares_are_attacked(
                squares=white_king_side_castle_occupancy, opponent_pieces=move_model.player_attr.opponent_pieces,
                side=PlayerSide.WHITE, board_state=move_model.fen.game_board) and not squares_are_occupied(
                board_state=board_state, squares=white_king_side_castle_occupancy):
            castle_moves.append(
                encode_move(source_square=white_king_position,
                            target_square=Positions.g1,
                            piece_name=PieceName.KING,
                            promotion_piece_name=PieceName.NONE,
                            capture_flag=False,
                            double_push_flag=False,
                            enpassant_flag=False,
                            castle_flag=True))
    return castle_moves
