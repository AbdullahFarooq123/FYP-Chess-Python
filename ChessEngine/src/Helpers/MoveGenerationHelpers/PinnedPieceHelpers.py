from ChessEngine.src.Enums.DirectionsEnum import \
    Direction
from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Enums.PieceNameEnum import PieceName
from ChessEngine.src.Helpers.BeautifyHelpers.GameBeautifyHelpers import print_bitboard
from ChessEngine.src.Helpers.MoveGenerationHelpers.OpponentMoveHelpers import \
    get_alignment_wrt_each_other
from ChessEngine.src.Helpers.PreCalculationHelpers.BishopPreCalHelpers import get_bishop_attacks
from ChessEngine.src.Helpers.PreCalculationHelpers.QueenPreCalHelpers import get_queen_attacks
from ChessEngine.src.Helpers.PreCalculationHelpers.RookPreCalHelpers import get_rook_attacks
from ChessEngine.src.Models.PinnedPieceModel import PinnedPiece
from ChessEngine.src.Models.RelativeDirectionModel import RelativeDirection
from ChessEngine.src.Helpers.PreCalculationHelpers.BitManipulationHelpers import get_least_bit_index, unsigned
from ChessEngine.src.Root.PreCalculationsData import directional_rays, square_bitmask

print_bitboard


def get_pinned_pieces(king_rays: int, player_pieces: list[int], king_position: Positions,
                      opponent_sliding_pieces_list: list[int], board_state: int, player_state: int,
                      opponent_state: int) -> PinnedPiece:
    pinned_piece_model: PinnedPiece = PinnedPiece()
    for player_piece_name in list(PieceName)[:-1]:
        player_piece: int = player_pieces[player_piece_name.value]
        player_piece &= king_rays
        while player_piece:
            player_piece_position: Positions = Positions(get_least_bit_index(player_piece))
            relative_dir_to_player_piece: RelativeDirection = get_alignment_wrt_each_other(king_position,
                                                                                           player_piece_position)
            for opponent_piece_name in list(PieceName)[2:5]:
                opponent_piece: int = opponent_sliding_pieces_list[opponent_piece_name.value - 2]
                while opponent_piece:
                    opponent_piece_position: Positions = Positions(get_least_bit_index(opponent_piece))
                    relative_dir_to_opponent_piece: RelativeDirection = get_alignment_wrt_each_other(king_position,
                                                                                                     opponent_piece_position)
                    if __validate_opponent_piece_alignment(opponent_piece_name=opponent_piece_name,
                                                           p2_position_wrt_p1=relative_dir_to_opponent_piece.p2_position_wrt_p1,
                                                           p1_position_wrt_p2=relative_dir_to_player_piece.p2_position_wrt_p1):
                        opponent_piece_ray_in_king_dir = \
                            directional_rays[relative_dir_to_opponent_piece.p1_position_wrt_p2.value][
                                opponent_piece_position.value] | square_bitmask[opponent_piece_position.value]
                        opponent_rays_with_occupancy = get_queen_attacks(opponent_piece_position.value,
                                                                         board_state) & unsigned(~opponent_state) | \
                                                       square_bitmask[opponent_piece_position.value]
                        player_piece_ray_in_opponent_piece_dir = \
                            directional_rays[relative_dir_to_player_piece.p2_position_wrt_p1.value][
                                player_piece_position.value]
                        if opponent_piece_name is PieceName.ROOK:
                            player_rays_with_occupancy = get_rook_attacks(player_piece_position.value,
                                                                          board_state) & unsigned(~player_state)
                        elif opponent_piece_name is PieceName.BISHOP:
                            player_rays_with_occupancy = get_bishop_attacks(player_piece_position.value,
                                                                            board_state) & unsigned(~player_state)
                        elif opponent_piece_name is PieceName.QUEEN:
                            player_rays_with_occupancy = get_queen_attacks(player_piece_position.value,
                                                                           board_state) & unsigned(~player_state)
                        if (opponent_piece_ray_in_king_dir & opponent_rays_with_occupancy) & (
                                player_piece_ray_in_opponent_piece_dir & player_rays_with_occupancy):
                            pinned_piece_model.add_piece(player_piece_position,
                                                         (
                                                                 opponent_piece_ray_in_king_dir) |
                                                         square_bitmask[opponent_piece_position.value])
                    opponent_piece &= opponent_piece - 1
            player_piece &= player_piece - 1
    return pinned_piece_model


def validate_for_pinned(is_pinned: bool, move: Positions, attacker_rays: int) -> Positions:
    if is_pinned:
        filtered_move: int = square_bitmask[move.value] & attacker_rays
        if filtered_move:
            return Positions(get_least_bit_index(filtered_move))
        else:
            return Positions.OUT_OF_BOUNDS
    return move


def __validate_opponent_piece_alignment(opponent_piece_name: PieceName, p2_position_wrt_p1: Direction,
                                        p1_position_wrt_p2: Direction):
    return (opponent_piece_name in [PieceName.QUEEN, PieceName.ROOK] and p2_position_wrt_p1 in
            list(Direction)[:4] and p2_position_wrt_p1 == p1_position_wrt_p2) or (
            opponent_piece_name in [PieceName.QUEEN, PieceName.BISHOP] and p2_position_wrt_p1 in list(
        Direction)[4:8] and p2_position_wrt_p1 == p1_position_wrt_p2)
