from typing import List

from ChessEngine.src.Enums.PlayerSideEnum import PlayerSide
from ChessEngine.src.Models.FenModel import Fen
from ChessEngine.src.Helpers.GenerateMoveHelpers.BlackCastle import \
    get_black_castle_moves
from ChessEngine.src.Helpers.GenerateMoveHelpers.King import get_king_moves
from ChessEngine.src.Helpers.GenerateMoveHelpers.WhiteCastle import \
    get_white_castle_moves
from ChessEngine.src.Helpers.GenerateMoveHelpers.Knight import get_knight_moves
from ChessEngine.src.Helpers.GenerateMoveHelpers.BlackPawn import get_black_pawn_moves
from ChessEngine.src.Helpers.GenerateMoveHelpers.WhitePawn import get_white_pawn_moves
from ChessEngine.src.Helpers.GenerateMoveHelpers.Bishop import get_bishop_moves
from ChessEngine.src.Helpers.GenerateMoveHelpers.Queen import get_queen_moves
from ChessEngine.src.Helpers.GenerateMoveHelpers.Rook import get_rook_moves
from ChessEngine.src.Models.GameStateModel import GameState


def get_moves_by_fen(fen: Fen) -> List[int]:
    move_model: GameState = GameState(fen)
    return get_moves_by_game_state(move_model=move_model)


def get_moves_by_game_state(move_model: GameState) -> List[int]:
    # moves List
    player_moves: List[int] = []
    turn: PlayerSide = move_model.player_attr.player_side
    check_count: int = move_model.attack_on_king_attr.check_count
    if check_count < 2:
        # ===================================white specific moves===================================
        if turn is PlayerSide.WHITE:
            player_moves += get_white_pawn_moves(move_model)
            player_moves += get_white_castle_moves(move_model)
        else:
            player_moves += get_black_pawn_moves(move_model)
            player_moves += get_black_castle_moves(move_model)
        # ===================================Player Non-Specific Moves===================================
        player_moves += get_knight_moves(move_model)
        player_moves += get_rook_moves(move_model)
        player_moves += get_bishop_moves(move_model)
        player_moves += get_queen_moves(move_model)
    player_moves += get_king_moves(move_model)
    return player_moves
