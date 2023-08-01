from typing import List

from ChessEngine.src.Enums.DirectionsEnum import \
    Direction
from ChessEngine.src.Enums.PieceNameEnum import PieceName
from ChessEngine.src.Enums.PlayerSideEnum import PlayerSide
from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Helpers.MoveEncryptionHelpers.EncodeMoveHelpers import encode_move
from ChessEngine.src.Helpers.MoveGenerationHelpers.MoveHelpers import \
    get_enpassant_move
from ChessEngine.src.Helpers.MoveGenerationHelpers.PinnedPieceHelpers import \
    validate_for_pinned
from ChessEngine.src.Helpers.PreCalculationHelpers.BitManipulationHelpers import get_least_bit_index, \
    move_bit_by_direction
from ChessEngine.src.Models.GameStateModel import GameState
from ChessEngine.src.Root.Const import before_top_edge, before_bottom_edge
from ChessEngine.src.Root.PreCalculationsData import square_bitmask, pawn_attack_maps


def get_white_pawn_moves(move_model: GameState) -> List[int]:
    pawn = move_model.fen.white_pieces[int(PieceName.PAWN.value)]
    pawn_moves = []
    # ===================================pawn moves===================================
    while pawn and move_model.attack_on_king_attr.check_count < 2:
        # Position and mask of pawn's position
        pawn_position: Positions = Positions(get_least_bit_index(pawn))
        pawn_positional_mask: int = square_bitmask[pawn_position.value]
        is_pinned: bool = bool(move_model.pinned_pieces.pinned_pieces & pawn_positional_mask)
        # If the move is promotion move
        promotion: bool = bool(pawn_positional_mask & before_top_edge)
        # get pawn attack map and validate it
        pawn_attack_map = pawn_attack_maps[PlayerSide.WHITE.value][pawn_position.value]
        pawn_attack_map &= move_model.fen.black_board
        for attacker in move_model.attack_on_king_attr.attackers:
            pawn_attack_map &= square_bitmask[attacker[0].value]
        # generate pawn quite move and validate it
        quite_move: int = move_bit_by_direction(pawn_positional_mask, Direction.NORTH)
        quite_move &= move_model.board_inverse
        # generate pawn double push move and validate it
        double_push_move: int = 0
        if pawn_positional_mask & before_bottom_edge:
            double_push_move: int = move_bit_by_direction(quite_move, Direction.NORTH)
            double_push_move &= move_model.board_inverse
        if move_model.attack_on_king_attr.check_count == 1 and any(
                attacker[1] in [PieceName.PAWN, PieceName.KNIGHT] for attacker in
                move_model.attack_on_king_attr.attackers):
            quite_move: int = 0
            double_push_move: int = 0
        # get enpassant move
        en_passant_move: Positions = get_enpassant_move(enpassant_square=move_model.fen.enpassant_square_position,
                                                        previous_move=move_model.previous_move)
        # set piece limit if the move is promotion one
        piece_length = list(PieceName)[1:5] if promotion else list(PieceName)[0:1]
        if is_pinned:
            pawn_attack_map &= move_model.pinned_pieces.attackers_ray
        # ===================================pawn attack moves===================================
        while pawn_attack_map:
            # get attack square as Position
            attack_square: Positions = Positions(get_least_bit_index(pawn_attack_map))
            # store moves for attack promotion or normal attack moves
            for piece_name in piece_length:
                pawn_moves.append(
                    encode_move(source_square=pawn_position,
                                target_square=attack_square,
                                piece_name=PieceName.PAWN,
                                promotion_piece_name=piece_name if promotion else PieceName.NONE,
                                capture_flag=True,
                                double_push_flag=False,
                                enpassant_flag=False,
                                castle_flag=False))
            pawn_attack_map &= pawn_attack_map - 1
        # ===================================pawn quite & double push===================================
        # get quite move as Positions
        quite_move: Positions = Positions(get_least_bit_index(quite_move))
        # if quite move exists
        if quite_move != Positions.OUT_OF_BOUNDS:
            quite_move: Positions = validate_for_pinned(is_pinned=is_pinned, move=quite_move,
                                                        attacker_rays=move_model.pinned_pieces.attackers_ray)
            # store moves for promotion or quite moves
            if (square_bitmask[quite_move.value] & move_model.attack_on_king_attr.attackers_ray) and \
                    quite_move != Positions.OUT_OF_BOUNDS:
                for piece_name in piece_length:
                    pawn_moves.append(
                        encode_move(source_square=pawn_position,
                                    target_square=quite_move,
                                    piece_name=PieceName.PAWN,
                                    promotion_piece_name=piece_name if promotion else PieceName.NONE,
                                    capture_flag=False,
                                    double_push_flag=False,
                                    enpassant_flag=False,
                                    castle_flag=False))
            # get double push as Positions
            double_push_move: Positions = Positions(get_least_bit_index(double_push_move))
            # if double push exists
            if double_push_move != Positions.OUT_OF_BOUNDS:
                # store move as double push move
                double_push_move: Positions = validate_for_pinned(is_pinned=is_pinned, move=double_push_move,
                                                                  attacker_rays=move_model.pinned_pieces.attackers_ray)
                if square_bitmask[double_push_move.value] & move_model.attack_on_king_attr.attackers_ray and \
                        double_push_move != Positions.OUT_OF_BOUNDS:
                    pawn_moves.append(
                        encode_move(source_square=pawn_position,
                                    target_square=double_push_move,
                                    piece_name=PieceName.PAWN,
                                    promotion_piece_name=PieceName.NONE,
                                    capture_flag=False,
                                    double_push_flag=True,
                                    enpassant_flag=False,
                                    castle_flag=False))
        # ===================================enpassant move===================================
        # if enpassant exists
        if en_passant_move != Positions.OUT_OF_BOUNDS:
            en_passant_move: Positions = validate_for_pinned(is_pinned=is_pinned, move=en_passant_move,
                                                             attacker_rays=move_model.pinned_pieces.attackers_ray)
            if en_passant_move != Positions.OUT_OF_BOUNDS:

                possible_opponent_position: Positions = Positions(en_passant_move.value - 8)
                # create mask of opponent position w.r.t enpassant square
                possible_opponent_position_mask: int = square_bitmask[possible_opponent_position.value]
                # if piece exists at location and difference btw opponent and player piece position is 1
                if (possible_opponent_position_mask & move_model.player_attr.opponent_pieces[
                    PieceName.PAWN.value]) and (
                        abs(pawn_position.value - possible_opponent_position.value) == 1):
                    # add enpassant move into the list
                    pawn_moves.append(
                        encode_move(source_square=pawn_position,
                                    target_square=en_passant_move,
                                    piece_name=PieceName.PAWN,
                                    promotion_piece_name=PieceName.NONE,
                                    capture_flag=False,
                                    double_push_flag=False,
                                    enpassant_flag=True,
                                    castle_flag=False))
        pawn &= pawn - 1
    return pawn_moves
