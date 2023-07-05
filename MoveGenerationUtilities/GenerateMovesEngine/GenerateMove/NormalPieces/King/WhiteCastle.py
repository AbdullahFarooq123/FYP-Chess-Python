from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from DebugUtilities.GameDependency.PieceDependency.PieceNameDependency import PieceName
from DebugUtilities.GameDependency.PlayerDependency.PlayerSideDependency import PlayerSide
from MoveGenerationUtilities.Const import white_queen_side_castle_occupancy, white_king_side_castle_occupancy
from MoveGenerationUtilities.EncryptionDependency.MoveEncryptions.EncodeMove import encode_move
from MoveGenerationUtilities.GenerateMovesEngine.MoveGenerationDependencies.CastleRightsDependencies import \
    squares_are_attacked
from MoveGenerationUtilities.GenerateMovesEngine.MoveGenerationModels.MovesModel import GameStateModel
from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import get_least_bit_index


def get_white_castle_moves(move_model: GameStateModel) -> list[int]:
    white_king: int = move_model.fen.white_pieces[PieceName.KING.value]
    white_king_position: Positions = Positions(get_least_bit_index(white_king))
    castle_moves: list[int] = []
    if move_model.white_castle.can_castle() and move_model.attack_on_king_attr.check_count == 0:
        if move_model.white_castle.can_queen_side_castle() and not squares_are_attacked(
                squares=white_queen_side_castle_occupancy, opponent_pieces=move_model.player_attr.opponent_pieces,
                side=PlayerSide.WHITE, board_state=move_model.fen.game_board):
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
                side=PlayerSide.WHITE, board_state=move_model.fen.game_board):
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
