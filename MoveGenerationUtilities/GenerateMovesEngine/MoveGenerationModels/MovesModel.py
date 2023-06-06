from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from DebugUtilities.GameDependency.PieceDependency.PieceNameDependency import PieceName
from DebugUtilities.GameDependency.PlayerDependency.PlayerSideDependency import PlayerSide
from FenUtilities.FenModel import Fen
from MoveGenerationUtilities.GenerateMovesEngine.MoveGenerationDependencies.GeneralDependencies import \
    get_player_wise_pieces_and_sides, get_sliding_pieces, get_sliding_pieces_list
from MoveGenerationUtilities.GenerateMovesEngine.MoveGenerationDependencies.GetAttackersDependencies import \
    get_opponent_attacks_and_find_check
from MoveGenerationUtilities.GenerateMovesEngine.MoveGenerationDependencies.PinnedPiecesDependencies import \
    get_pinned_pieces
from MoveGenerationUtilities.GenerateMovesEngine.MoveGenerationModels.AttackOnKingModel import AttackOnKing
from MoveGenerationUtilities.GenerateMovesEngine.MoveGenerationModels.CastleModel import Castle
from MoveGenerationUtilities.GenerateMovesEngine.MoveGenerationModels.PinnedPieceModel import PinnedPiece
from MoveGenerationUtilities.GenerateMovesEngine.MoveGenerationModels.PlayerAttributesModel import PlayerAttribute

from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import unsigned, get_least_bit_index
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import rook_attacks, bishop_attacks


class MoveDependencyModel:
    def __init__(self, fen: Fen, previous_move: int):
        self.fen = fen
        self.white_castle = Castle(fen.white_castle)
        self.black_castle = Castle(fen.black_castle)
        self.previous_move = previous_move
        self.board_inverse = unsigned(~fen.game_board)
        # decide opponent and player pieces
        self.player_attr: PlayerAttribute = get_player_wise_pieces_and_sides(
            white_pieces=fen.white_pieces, black_pieces=fen.black_pieces, turn=fen.player_turn)
        # get the bitmask of player's king
        self.opponent_sliding_pieces = get_sliding_pieces(piece_list=self.player_attr.opponent_pieces)
        self.opponent_sliding_pieces_list = get_sliding_pieces_list(piece_list=self.player_attr.opponent_pieces)
        self.player_king_mask = self.player_attr.player_pieces[PieceName.KING.value]
        self.player_king_pos: Positions = Positions(get_least_bit_index(self.player_king_mask))
        self.king_rays = bishop_attacks[self.player_king_pos.value] | rook_attacks[
            self.player_king_pos.value]
        self.pinned_pieces: PinnedPiece = get_pinned_pieces(king_rays=self.king_rays,
                                                            player_pieces=self.player_attr.player_pieces,
                                                            king_position=self.player_king_pos,
                                                            opponent_sliding_pieces_list=self.opponent_sliding_pieces_list)
        # get opponent attack mask, no of checks and the list of attackers as (Name, Position)
        self.attack_on_king_attr: AttackOnKing = get_opponent_attacks_and_find_check(
            opponent_pieces=self.player_attr.opponent_pieces,
            player_king_mask=self.player_king_mask,
            opponent_side=self.player_attr.opponent_side,
            board_state=fen.game_board,
            king_position=self.player_king_pos)
