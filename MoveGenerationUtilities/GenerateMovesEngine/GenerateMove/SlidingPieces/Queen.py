from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from DebugUtilities.GameDependency.PieceDependency.PieceNameDependency import PieceName
from DebugUtilities.GameDependency.PlayerDependency.PlayerSideDependency import PlayerSide
from MoveGenerationUtilities.EncryptionDependency.MoveEncryptions.EncodeMove import encode_move
from MoveGenerationUtilities.GenerateMovesEngine.MoveGenerationDependencies.GetAttackersDependencies import \
    is_sliding_piece
from MoveGenerationUtilities.GenerateMovesEngine.MoveGenerationModels.MovesModel import GameStateModel
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Queen import get_queen_attacks
from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import get_least_bit_index, unsigned
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import square_bitmask


def get_queen_moves(move_model: GameStateModel) -> list[int]:
    queen: int = (move_model.fen.white_pieces if move_model.player_attr.player_side == PlayerSide.WHITE else
                  move_model.fen.black_pieces)[PieceName.QUEEN.value]
    queen_moves: list[int] = []
    while queen:
        queen_position: Positions = Positions(get_least_bit_index(queen))
        queen_mask = square_bitmask[queen_position.value]
        is_pinned: bool = bool(queen_mask & move_model.pinned_pieces.pinned_pieces)
        queen_attack: int = get_queen_attacks(position=queen_position.value, occupancy=move_model.fen.game_board)
        queen_attack &= unsigned(~move_model.player_attr.player_state)
        if move_model.attack_on_king_attr.check_count == 1:
            if is_sliding_piece(move_model.attack_on_king_attr.attackers[0][1]):
                queen_attack &= move_model.attack_on_king_attr.attackers_ray
            else:
                queen_attack &= move_model.attack_on_king_attr.attackers_bitmask
        if is_pinned:
            queen_attack &= move_model.pinned_pieces.attackers_ray

        while queen_attack:
            target_square: Positions = Positions(get_least_bit_index(queen_attack))
            capture_flag: bool = bool(square_bitmask[target_square.value] & move_model.player_attr.opponent_state)
            queen_moves.append(
                encode_move(source_square=queen_position,
                            target_square=target_square,
                            piece_name=PieceName.QUEEN,
                            promotion_piece_name=PieceName.NONE,
                            capture_flag=capture_flag,
                            double_push_flag=False,
                            enpassant_flag=False,
                            castle_flag=False))
            queen_attack &= queen_attack - 1
        queen &= queen - 1
    return queen_moves
