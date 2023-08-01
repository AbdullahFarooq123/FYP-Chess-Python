from typing import List

from ChessEngine.src.Enums.PieceNameEnum import PieceName
from ChessEngine.src.Enums.PlayerSideEnum import PlayerSide
from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Helpers.MoveGenerationHelpers.MoveHelpers import \
    get_player_wise_pieces_and_sides, get_sliding_pieces, get_sliding_pieces_list
from ChessEngine.src.Helpers.MoveGenerationHelpers.OpponentMoveHelpers import \
    get_opponent_attacks_and_find_check
from ChessEngine.src.Helpers.MoveGenerationHelpers.PinnedPieceHelpers import \
    get_pinned_pieces
from ChessEngine.src.Helpers.PreCalculationHelpers.BitManipulationHelpers import unsigned, get_least_bit_index
from ChessEngine.src.Helpers.PreCalculationHelpers.QueenPreCalHelpers import get_queen_attacks
from ChessEngine.src.Models.AttackOnKingModel import AttackOnKing
from ChessEngine.src.Models.CastleModel import Castle
from ChessEngine.src.Models.FenModel import Fen
from ChessEngine.src.Models.PinnedPieceModel import PinnedPiece
from ChessEngine.src.Models.PlayerAttributesModel import PlayerAttribute


class GameState:
    def __init__(self, fen: Fen):
        self.fen: Fen = fen
        self.white_castle: Castle = Castle(self.fen.white_castle)
        self.black_castle: Castle = Castle(self.fen.black_castle)
        self.moves: List[int] = []
        self.recalculate()

    def recalculate(self, change_turn: bool = False):
        if change_turn:
            self.__change_turn()
        self.previous_move = 0 if len(self.moves) == 0 else self.moves[len(self.moves) - 1]
        self.board_inverse = unsigned(~self.fen.game_board)
        # decide opponent and player pieces
        self.player_attr: PlayerAttribute = get_player_wise_pieces_and_sides(
            white_pieces=self.fen.white_pieces, white_state=self.fen.white_board, black_pieces=self.fen.black_pieces,
            black_state=self.fen.black_board, turn=self.fen.player_turn)
        # get the bitmask of player's king
        self.opponent_sliding_pieces = get_sliding_pieces(piece_list=self.player_attr.opponent_pieces)
        self.opponent_sliding_pieces_list = get_sliding_pieces_list(piece_list=self.player_attr.opponent_pieces)
        self.player_king_mask = self.player_attr.player_pieces[PieceName.KING.value]
        self.player_king_pos: Positions = Positions(get_least_bit_index(self.player_king_mask))
        self.king_rays = get_queen_attacks(position=self.player_king_pos.value, occupancy=self.fen.game_board)
        self.pinned_pieces: PinnedPiece = get_pinned_pieces(king_rays=self.king_rays,
                                                            player_pieces=self.player_attr.player_pieces,
                                                            king_position=self.player_king_pos,
                                                            opponent_sliding_pieces_list=self.opponent_sliding_pieces_list,
                                                            board_state=self.fen.game_board,
                                                            player_state=self.player_attr.player_state,
                                                            opponent_state=self.player_attr.opponent_state)
        # get opponent attack mask, no of checks and the list of attackers as (Name, Position)
        self.attack_on_king_attr: AttackOnKing = get_opponent_attacks_and_find_check(
            opponent_pieces=self.player_attr.opponent_pieces,
            player_king_mask=self.player_king_mask,
            opponent_side=self.player_attr.opponent_side,
            board_state=self.fen.game_board,
            player_king_position=self.player_king_pos)
        self.fen.white_castle = self.white_castle.castle_rights
        self.fen.black_castle = self.black_castle.castle_rights
        from ChessEngine.src.Controllers.GenerateMovesController import get_moves_by_game_state
        self.moves = get_moves_by_game_state(self)

    def __change_turn(self):
        self.fen.player_turn = PlayerSide.BLACK if self.fen.player_turn is PlayerSide.WHITE else PlayerSide.WHITE

    def copy(self):
        return GameState(self.fen)

    def is_checkmate(self):
        return bool(self.attack_on_king_attr.check_count) and len(self.moves) == 0

    def is_stalemate(self):
        return bool(self.attack_on_king_attr.check_count) and len(self.moves) == 0

    def low_on_material(self):
        opponent_pieces = self.player_attr.opponent_pieces
        for piece_name in list(PieceName)[:-2]:
            if bool(opponent_pieces[piece_name.value]):
                return False
        sufficient_pieces = [PieceName.QUEEN, PieceName.ROOK, PieceName.PAWN]
        player_pieces = self.player_attr.player_pieces
        for piece_name in sufficient_pieces:
            if bool(player_pieces[piece_name.value]):
                return False
        knight_exists = bool(player_pieces[PieceName.KNIGHT.value])
        bishop_exists = bool(player_pieces[PieceName.BISHOP.value])
        if bishop_exists and knight_exists:
            return False
        return True

    def is_game_over(self):
        return self.is_checkmate() or self.is_stalemate() or self.low_on_material()
