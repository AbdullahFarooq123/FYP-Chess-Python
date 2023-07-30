from ChessEngine.src.Enums.DirectionsEnum import Direction
from ChessEngine.src.Enums.PieceNameEnum import PieceName
from ChessEngine.src.Enums.PlayerSideEnum import PlayerSide
from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Models.AttackOnKingModel import AttackOnKing
from ChessEngine.src.Models.RelativeDirectionModel import RelativeDirection
from ChessEngine.src.Helpers.PreCalculationHelpers.BishopPreCalHelpers import get_bishop_attacks
from ChessEngine.src.Helpers.PreCalculationHelpers.QueenPreCalHelpers import get_queen_attacks
from ChessEngine.src.Helpers.PreCalculationHelpers.RookPreCalHelpers import get_rook_attacks
from ChessEngine.src.Helpers.PreCalculationHelpers.BitManipulationHelpers import unsigned, get_least_bit_index
from ChessEngine.src.Root.PreCalculationsData import directional_rays, pawn_attack_maps, \
    knight_attack_maps, king_attack_maps, square_bitmask


def get_opponent_attacks_and_find_check(opponent_pieces: list, player_king_mask: int, opponent_side: PlayerSide,
                                        board_state: int, player_king_position: Positions) -> AttackOnKing:
    attackers: list[tuple[Positions, PieceName]] = []
    check_count: int = 0
    attackers_ray = 0
    attackers_mask = 0
    opponent_attacks = 0
    virtual_occupancy = board_state & ~player_king_mask
    for piece_name in list(PieceName)[:-2]:
        opponent_piece_mask: int = opponent_pieces[piece_name.value]
        while opponent_piece_mask:
            piece_position: Positions = Positions(get_least_bit_index(opponent_piece_mask))
            piece_bitmask = square_bitmask[piece_position.value]
            piece_attacks: int = 0
            virtual_piece_attacks: int = 0
            if piece_name == PieceName.PAWN:
                piece_attacks: int = pawn_attack_maps[opponent_side.value][piece_position.value]
                virtual_piece_attacks |= piece_attacks
            elif piece_name == PieceName.KNIGHT:
                piece_attacks: int = knight_attack_maps[piece_position.value]
                virtual_piece_attacks |= piece_attacks
            elif piece_name == PieceName.BISHOP:
                piece_attacks: int = get_bishop_attacks(piece_position.value, board_state)
                virtual_piece_attacks |= get_bishop_attacks(piece_position.value, virtual_occupancy)
            elif piece_name == PieceName.ROOK:
                piece_attacks: int = get_rook_attacks(piece_position.value, board_state)
                virtual_piece_attacks |= get_rook_attacks(piece_position.value, virtual_occupancy)
            elif piece_name == PieceName.QUEEN:
                piece_attacks: int = get_queen_attacks(piece_position.value, board_state)
                virtual_piece_attacks |= get_queen_attacks(piece_position.value, virtual_occupancy)
            elif piece_name == PieceName.KING:
                piece_attacks: int = king_attack_maps[piece_position.value]
                virtual_piece_attacks |= piece_attacks
            opponent_attacks |= virtual_piece_attacks
            if piece_attacks & player_king_mask:
                check_count += 1
                attackers.append((piece_position, piece_name))
                attackers_mask |= piece_bitmask
                if is_sliding_piece(piece_name):
                    attackers_ray |= __get_valid_attack_ray(piece_name, piece_position, player_king_position)
            opponent_piece_mask &= opponent_piece_mask - 1
    if attackers_ray == 0:
        attackers_ray = unsigned(~attackers_ray)
    if attackers_mask == 0:
        attackers_mask = unsigned(~attackers_mask)
    return AttackOnKing(attackers_ray=attackers_ray, check_count=check_count, attackers=attackers,
                        attackers_bitmask=attackers_mask, opponent_attacks=opponent_attacks)


def is_sliding_piece(piece_name: PieceName) -> bool:
    return piece_name in [PieceName.ROOK, PieceName.BISHOP, PieceName.QUEEN]


def __get_valid_attack_ray(attacker_piece_name: PieceName, attacker_position: Positions,
                           king_position: Positions) -> int:
    directions_info: RelativeDirection = get_alignment_wrt_each_other(attacker_position, king_position)
    if __validate_piece_with_dir_and_pos(attacker_piece_name, directions_info):
        attacker_ray = directional_rays[directions_info.p2_position_wrt_p1.value][attacker_position.value] | \
                       square_bitmask[attacker_position.value]
        king_ray = directional_rays[directions_info.p1_position_wrt_p2.value][king_position.value]
        return attacker_ray & king_ray
    return unsigned(~0)


def __validate_piece_with_dir_and_pos(attacker_piece_name: PieceName, dir_info: RelativeDirection) -> bool:
    return (attacker_piece_name in [PieceName.QUEEN, PieceName.BISHOP] and dir_info.is_diagonal_aligned()) or (
            attacker_piece_name in [PieceName.QUEEN,
                                    PieceName.ROOK] and dir_info.is_horizontal_aligned()) and dir_info.is_aligned()


def get_alignment_wrt_each_other(p1_position: Positions, p2_position: Positions) -> RelativeDirection:
    file_diff = p2_position.value % 8 - p1_position.value % 8
    rank_diff = p2_position.value // 8 - p1_position.value // 8

    # Check if both pieces are in the same position
    if file_diff == 0 and rank_diff == 0:
        return RelativeDirection(p1_position_wrt_p2=Direction.NOT_ALIGNED,
                                 p2_position_wrt_p1=Direction.NOT_ALIGNED)

    # Check the relative position based on the file and rank differences
    if abs(rank_diff) == abs(file_diff):
        if rank_diff > 0:
            if file_diff > 0:
                return RelativeDirection(p1_position_wrt_p2=Direction.SOUTH_EAST,
                                         p2_position_wrt_p1=Direction.NORTH_WEST)
            else:
                return RelativeDirection(p1_position_wrt_p2=Direction.SOUTH_WEST,
                                         p2_position_wrt_p1=Direction.NORTH_EAST)
        else:
            if file_diff > 0:
                return RelativeDirection(p1_position_wrt_p2=Direction.NORTH_EAST,
                                         p2_position_wrt_p1=Direction.SOUTH_WEST)
            else:
                return RelativeDirection(p1_position_wrt_p2=Direction.NORTH_WEST,
                                         p2_position_wrt_p1=Direction.SOUTH_EAST)
    elif rank_diff == 0:
        if file_diff > 0:
            return RelativeDirection(p1_position_wrt_p2=Direction.EAST,
                                     p2_position_wrt_p1=Direction.WEST)
        else:
            return RelativeDirection(p1_position_wrt_p2=Direction.WEST,
                                     p2_position_wrt_p1=Direction.EAST)
    elif file_diff == 0:
        if rank_diff > 0:
            return RelativeDirection(p1_position_wrt_p2=Direction.SOUTH,
                                     p2_position_wrt_p1=Direction.NORTH)
        else:
            return RelativeDirection(p1_position_wrt_p2=Direction.NORTH,
                                     p2_position_wrt_p1=Direction.SOUTH)
    else:
        return RelativeDirection(p1_position_wrt_p2=Direction.NOT_ALIGNED,
                                 p2_position_wrt_p1=Direction.NOT_ALIGNED)
