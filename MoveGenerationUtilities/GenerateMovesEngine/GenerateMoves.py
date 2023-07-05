from DebugUtilities.GameDependency.PlayerDependency.PlayerSideDependency import PlayerSide
from FenUtilities.FenModel import Fen
from MoveGenerationUtilities.GenerateMovesEngine.GenerateMove.NormalPieces.King.BlackCastle import \
    get_black_castle_moves
from MoveGenerationUtilities.GenerateMovesEngine.GenerateMove.NormalPieces.King.WhiteCastle import \
    get_white_castle_moves
from MoveGenerationUtilities.GenerateMovesEngine.GenerateMove.NormalPieces.Pawn.BlackPawn import get_black_pawn_moves
from MoveGenerationUtilities.GenerateMovesEngine.GenerateMove.NormalPieces.Pawn.WhitePawn import get_white_pawn_moves
from MoveGenerationUtilities.GenerateMovesEngine.GenerateMove.SlidingPieces.Bishop import get_bishop_moves
from MoveGenerationUtilities.GenerateMovesEngine.GenerateMove.SlidingPieces.Queen import get_queen_moves
from MoveGenerationUtilities.GenerateMovesEngine.GenerateMove.SlidingPieces.Rook import get_rook_moves
from MoveGenerationUtilities.GenerateMovesEngine.MoveGenerationModels.MovesModel import GameStateModel


def get_moves(fen: Fen, previous_move: int) -> list:
    # moves list
    player_moves = []
    move_model = GameStateModel(fen)
    # ===================================white specific moves===================================
    if move_model.player_attr.player_side == PlayerSide.WHITE and move_model.attack_on_king_attr.check_count < 2:
        player_moves += get_white_pawn_moves(move_model)
        player_moves += get_white_castle_moves(move_model)
    else:
        player_moves += get_black_pawn_moves(move_model)
        player_moves += get_black_castle_moves(move_model)
    # ===================================Player Non-Specific Moves===================================
    player_moves += get_rook_moves(move_model)
    player_moves += get_bishop_moves(move_model)
    player_moves += get_queen_moves(move_model)
    return player_moves
