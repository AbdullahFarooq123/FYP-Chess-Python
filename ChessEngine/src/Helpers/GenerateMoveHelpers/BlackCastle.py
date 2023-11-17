from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Enums.PieceNameEnum import PieceName
from ChessEngine.src.Enums.PlayerSideEnum import PlayerSide
from ChessEngine.src.Root.Const import black_queen_side_castle_occupancy, black_king_side_castle_occupancy
from ChessEngine.src.Helpers.MoveEncryptionHelpers.EncodeMoveHelpers import encode_move
from ChessEngine.src.Helpers.MoveGenerationHelpers.CastleMoveHelpers import \
    squares_are_attacked, squares_are_occupied
from ChessEngine.src.Models.GameStateModel import GameState
from ChessEngine.src.Helpers.PreCalculationHelpers.BitManipulationHelpers import get_least_bit_index


def get_black_castle_moves(move_model: GameState) -> list[int]:
    black_king: int = move_model.fen.black_pieces[PieceName.KING.value]
    black_king_position: Positions = Positions(get_least_bit_index(black_king))
    castle_moves: list[int] = []
    board_state: int = move_model.fen.game_board
    if move_model.black_castle.can_castle() and move_model.attack_on_king_attr.check_count == 0:
        if move_model.black_castle.can_queen_side_castle() and not squares_are_attacked(
                squares=black_queen_side_castle_occupancy, opponent_pieces=move_model.player_attr.opponent_pieces,
                side=PlayerSide.BLACK, board_state=move_model.fen.game_board) and not squares_are_occupied(
                board_state=board_state, squares=black_queen_side_castle_occupancy):
            castle_moves.append(
                encode_move(source_square=black_king_position,
                            target_square=Positions.c8,
                            piece_name=PieceName.KING,
                            promotion_piece_name=PieceName.NONE,
                            capture_flag=False,
                            double_push_flag=False,
                            enpassant_flag=False,
                            castle_flag=True))
        if move_model.black_castle.can_king_side_castle() and not squares_are_attacked(
                squares=black_king_side_castle_occupancy, opponent_pieces=move_model.player_attr.opponent_pieces,
                side=PlayerSide.BLACK, board_state=move_model.fen.game_board) and not squares_are_occupied(
                board_state=board_state, squares=black_king_side_castle_occupancy):
            castle_moves.append(
                encode_move(source_square=black_king_position,
                            target_square=Positions.g8,
                            piece_name=PieceName.KING,
                            promotion_piece_name=PieceName.NONE,
                            capture_flag=False,
                            double_push_flag=False,
                            enpassant_flag=False,
                            castle_flag=True))
    return castle_moves
