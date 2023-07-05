from DebugUtilities.GameDependency.BoardDependency.DirectionalDependency.SpecificDirectionDependency import \
    SpecificDirections
from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from DebugUtilities.GameDependency.PieceDependency.PieceNameDependency import PieceName
from MoveGenerationUtilities.GenerateMovesEngine.MoveGenerationDependencies.GetAttackersDependencies import \
    get_alignment_wrt_each_other
from MoveGenerationUtilities.GenerateMovesEngine.MoveGenerationModels.PinnedPieceModel import PinnedPiece
from MoveGenerationUtilities.GenerateMovesEngine.MoveGenerationModels.RelativeDirectionModel import RelativeDirection
from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import get_least_bit_index
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import rook_attacks_table, bishop_attacks_table, \
    directional_rays, square_bitmask


def get_pinned_pieces(king_rays: int, player_pieces: list[int], king_position: Positions,
                      opponent_sliding_pieces_list: list[int]) -> PinnedPiece:
    pinned_piece_model: PinnedPiece = PinnedPiece()
    for player_piece_name in list(PieceName)[:-1]:
        player_piece: int = player_pieces[player_piece_name.value]
        player_piece &= king_rays
        while player_piece:
            player_piece_position: Positions = Positions(get_least_bit_index(player_piece))
            relative_dir_to_player_piece: RelativeDirection = get_alignment_wrt_each_other(king_position,
                                                                                           player_piece_position)
            for opponent_piece_name in list(PieceName)[2:5]:
                opponent_piece: int = opponent_sliding_pieces_list[2 - opponent_piece_name.value]
                while opponent_piece:
                    opponent_piece_position: Positions = Positions(get_least_bit_index(opponent_piece))
                    relative_dir_to_opponent_piece: RelativeDirection = get_alignment_wrt_each_other(king_position,
                                                                                                     opponent_piece_position)
                    if __validate_opponent_piece_alignment(opponent_piece_name=opponent_piece_name,
                                                           p2_position_wrt_p1=relative_dir_to_opponent_piece.p2_position_wrt_p1,
                                                           p1_position_wrt_p2=relative_dir_to_player_piece.p2_position_wrt_p1):
                        opponent_piece_ray_in_king_dir = \
                            directional_rays[relative_dir_to_opponent_piece.p1_position_wrt_p2.value][
                                opponent_piece_position.value]
                        player_piece_ray_in_opponent_piece_dir = \
                            directional_rays[relative_dir_to_player_piece.p2_position_wrt_p1.value][
                                player_piece_position.value]
                        pinned_piece_model.add_piece(player_piece_position,
                                                     (
                                                             opponent_piece_ray_in_king_dir & player_piece_ray_in_opponent_piece_dir) |
                                                     square_bitmask[opponent_piece_position.value])
                    opponent_piece &= opponent_piece - 1
            player_piece &= player_piece - 1
    return pinned_piece_model


def validate_for_pinned(is_pinned: bool, move: Positions, attacker_rays: int) -> Positions:
    if is_pinned:
        filtered_move: int = square_bitmask[move.value] & attacker_rays
        if filtered_move:
            return Positions(filtered_move)
        else:
            return Positions.OUT_OF_BOUNDS
    return move


def __validate_opponent_piece_alignment(opponent_piece_name: PieceName, p2_position_wrt_p1: SpecificDirections,
                                        p1_position_wrt_p2: SpecificDirections):
    return (opponent_piece_name in [PieceName.QUEEN, PieceName.ROOK] and p2_position_wrt_p1 in
            list(SpecificDirections)[:4] and p2_position_wrt_p1 == p1_position_wrt_p2) or (
            opponent_piece_name in [PieceName.QUEEN, PieceName.BISHOP] and p2_position_wrt_p1 in list(
        SpecificDirections)[4:8] and p2_position_wrt_p1 == p1_position_wrt_p2)
