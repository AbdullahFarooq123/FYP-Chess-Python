from DebugUtilities.BeautifyDependency.GameBeautify import print_bitboard
from DebugUtilities.GameDependency.BoardDependency.DirectionalDependency.SpecificDirectionDependency import \
    SpecificDirections
from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from DebugUtilities.GameDependency.PieceDependency.PieceNameDependency import PieceName
from DebugUtilities.GameDependency.PlayerDependency.PlayerSideDependency import PlayerSide
from FenUtilities.FenModel import Fen
from MoveGenerationUtilities.Const import before_top_edge, before_bottom_edge, black_queen_side_castle_occupancy, \
    black_king_side_castle_occupancy
from MoveGenerationUtilities.Const import white_king_side_castle_occupancy, white_queen_side_castle_occupancy
from MoveGenerationUtilities.EncryptionDependency.MoveEncryptions.EncodeMove import encode_move
from MoveGenerationUtilities.GenerateMovesEngine.MoveGenerationDependencies.CastleRightsDependencies import \
    squares_are_attacked
from MoveGenerationUtilities.GenerateMovesEngine.MoveGenerationDependencies.GeneralDependencies import \
    get_enpassant_move
from MoveGenerationUtilities.GenerateMovesEngine.MoveGenerationDependencies.PinnedPiecesDependencies import \
    validate_for_pinned
from MoveGenerationUtilities.GenerateMovesEngine.MoveGenerationModels.MovesModel import MoveDependencyModel
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Rook import get_rook_attacks
from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import move_bit, get_least_bit_index, unsigned
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import square_bitmask, pawn_attack_maps


def get_moves(fen: Fen, previous_move: int) -> list:
    # moves list
    player_moves = []
    move_model = MoveDependencyModel(fen, previous_move)
    # ===================================white specific moves===================================
    if move_model.player_attr.player_side == PlayerSide.WHITE and move_model.attack_on_king_attr.check_count < 2:
        player_moves += get_white_pawn_moves(move_model)
        player_moves += get_white_castle_moves(move_model)
    else:
        player_moves += get_black_pawn_moves(move_model)
        player_moves += get_black_castle_moves(move_model)
    return player_moves


def get_white_pawn_moves(move_model: MoveDependencyModel) -> list[int]:
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
            pawn_attack_map &= attacker[0]
        # generate pawn quite move and validate it
        quite_move: int = move_bit(pawn_positional_mask, SpecificDirections.NORTH)
        quite_move &= move_model.board_inverse
        # generate pawn double push move and validate it
        double_push_move: int = 0
        if pawn_positional_mask & before_bottom_edge:
            double_push_move: int = move_bit(quite_move, SpecificDirections.NORTH)
            double_push_move &= move_model.board_inverse
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
            if (quite_move.value & move_model.attack_on_king_attr.attackers_ray) and \
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
                if double_push_move.value & move_model.attack_on_king_attr.attackers_ray and \
                        quite_move != Positions.OUT_OF_BOUNDS:
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
            if en_passant_move != Positions.OUT_OF_BOUNDS and move_model.attack_on_king_attr.check_count == 0:

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


def get_white_castle_moves(move_model: MoveDependencyModel) -> list[int]:
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


def get_black_pawn_moves(move_model: MoveDependencyModel) -> list[int]:
    pawn = move_model.fen.black_pieces[int(PieceName.PAWN.value)]
    pawn_moves = []
    # ===================================pawn moves===================================
    while pawn and move_model.attack_on_king_attr.check_count < 2:
        # Position and mask of pawn's position
        pawn_position: Positions = Positions(get_least_bit_index(pawn))
        pawn_positional_mask: int = square_bitmask[pawn_position.value]
        is_pinned: bool = bool(move_model.pinned_pieces.pinned_pieces & pawn_positional_mask)
        # If the move is promotion move
        promotion: bool = bool(pawn_positional_mask & before_bottom_edge)
        # get pawn attack map and validate it
        pawn_attack_map = pawn_attack_maps[PlayerSide.BLACK.value][pawn_position.value]
        pawn_attack_map &= move_model.fen.white_board
        for attacker in move_model.attack_on_king_attr.attackers:
            pawn_attack_map &= attacker[0]
        # generate pawn quite move and validate it
        quite_move: int = move_bit(pawn_positional_mask, SpecificDirections.SOUTH)
        quite_move &= move_model.board_inverse
        # generate pawn double push move and validate it
        double_push_move: int = 0
        if pawn_positional_mask & before_top_edge:
            double_push_move: int = move_bit(quite_move, SpecificDirections.SOUTH)
            double_push_move &= move_model.board_inverse
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
            if (quite_move.value & move_model.attack_on_king_attr.attackers_ray) and \
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
                if double_push_move.value & move_model.attack_on_king_attr.attackers_ray and \
                        quite_move != Positions.OUT_OF_BOUNDS:
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
            if en_passant_move != Positions.OUT_OF_BOUNDS and move_model.attack_on_king_attr.check_count == 0:

                possible_opponent_position: Positions = Positions(en_passant_move.value + 8)
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


def get_black_castle_moves(move_model: MoveDependencyModel) -> list[int]:
    black_king: int = move_model.fen.black_pieces[PieceName.KING.value]
    black_king_position: Positions = Positions(get_least_bit_index(black_king))
    castle_moves: list[int] = []
    if move_model.black_castle.can_castle() and move_model.attack_on_king_attr.check_count == 0:
        if move_model.black_castle.can_queen_side_castle() and not squares_are_attacked(
                squares=black_queen_side_castle_occupancy, opponent_pieces=move_model.player_attr.opponent_pieces,
                side=PlayerSide.BLACK, board_state=move_model.fen.game_board):
            castle_moves.append(
                encode_move(source_square=black_king_position,
                            target_square=Positions.c1,
                            piece_name=PieceName.KING,
                            promotion_piece_name=PieceName.NONE,
                            capture_flag=False,
                            double_push_flag=False,
                            enpassant_flag=False,
                            castle_flag=True))
        if move_model.black_castle.can_king_side_castle() and not squares_are_attacked(
                squares=black_king_side_castle_occupancy, opponent_pieces=move_model.player_attr.opponent_pieces,
                side=PlayerSide.BLACK, board_state=move_model.fen.game_board):
            castle_moves.append(
                encode_move(source_square=black_king_position,
                            target_square=Positions.g1,
                            piece_name=PieceName.KING,
                            promotion_piece_name=PieceName.NONE,
                            capture_flag=False,
                            double_push_flag=False,
                            enpassant_flag=False,
                            castle_flag=True))
    return castle_moves


def get_rook_moves(move_model: MoveDependencyModel) -> list[int]:
    rook: int = (move_model.fen.white_pieces if move_model.player_attr.player_side == PlayerSide.WHITE else
                 move_model.fen.black_pieces)[PieceName.ROOK.value]
    rook_moves: list[int] = []
    while rook:
        rook_mask = get_least_bit_index(rook)
        rook_position: Positions = Positions(rook_mask)
        is_pinned: bool = bool(rook_mask & move_model.pinned_pieces.pinned_pieces)
        rook_attack: int = get_rook_attacks(position=rook_position.value, occupancy=move_model.fen.game_board)
        # print_bitboard(move_model.fen.game_board)
        # print_bitboard(rook_mask)
        # print_bitboard(rook_attack)
        rook_attack &= unsigned(~move_model.player_attr.player_state)
        if move_model.attack_on_king_attr.check_count == 1:
            print_bitboard(rook_attack)
            print_bitboard(move_model.attack_on_king_attr.attackers_ray)
            print_bitboard(move_model.attack_on_king_attr.attackers_bitmask)
            rook_attack &= move_model.attack_on_king_attr.attackers_ray
            rook_attack &= move_model.attack_on_king_attr.attackers_bitmask
        if is_pinned:
            rook_attack &= move_model.pinned_pieces.attackers_ray

        while rook_attack:
            target_square: Positions = Positions(get_least_bit_index(rook_attack))
            rook_moves.append(
                encode_move(source_square=rook_position,
                            target_square=target_square,
                            piece_name=PieceName.KING,
                            promotion_piece_name=PieceName.NONE,
                            capture_flag=False,
                            double_push_flag=False,
                            enpassant_flag=False,
                            castle_flag=True))
            rook_attack &= rook_attack - 1
        rook &= rook - 1
    return rook_moves
