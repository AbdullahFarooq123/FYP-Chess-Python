import re
from typing import Optional, List

from ChessEngine.src.Helpers.BeautifyHelpers.GameBeautifyHelpers import white_pieces_char
from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Enums.PieceNameEnum import PieceName
from ChessEngine.src.Enums.PlayerSideEnum import PlayerSide
from ChessEngine.src.Models.EncryptionModel import Encryption
from ChessEngine.src.Helpers.MoveEncryptionHelpers.DecodeMoveHelpers import decode_move_all
from ChessEngine.src.Models.PGNModel import PGNModel


def parse_user_move(move: str, player_turn: PlayerSide) -> Optional[PGNModel]:
    piece_name: PieceName = PieceName.NONE
    source_square: Positions = Positions.OUT_OF_BOUNDS
    target_square: Positions = Positions.OUT_OF_BOUNDS
    capture_flag: bool = 'x' in move
    source_rank = ''
    source_file = ''
    move = re.sub(r'[x#+]|1-0|0-1|0-0', '', move)
    if len(move) == 0:
        return None
    index_of_promotion_piece_name = move.find('=')
    promotion_piece_ascii = '' if index_of_promotion_piece_name == -1 else move[index_of_promotion_piece_name + 1]
    promotion_piece_name: PieceName = PieceName.NONE if len(promotion_piece_ascii) == 0 else PieceName(
        white_pieces_char.find(promotion_piece_ascii))
    if len(promotion_piece_ascii) != 0:
        move = move.replace(f'={promotion_piece_ascii}', '')
    if 'O' in move:
        piece_name = PieceName.KING
        source_square = Positions.e1 if player_turn is PlayerSide.WHITE else Positions.e8
        if 'O-O-O' in move:
            target_square = Positions.c1 if player_turn is PlayerSide.WHITE else Positions.c8
        else:
            target_square = Positions.g1 if player_turn is PlayerSide.WHITE else Positions.g8
        return PGNModel(piece_name=piece_name,
                        source_square=source_square,
                        source_file=source_file,
                        source_rank=source_rank,
                        target_square=target_square,
                        promotion_piece_name=promotion_piece_name,
                        capture_flag=False,
                        castle_flag=True)
    if move[0] in white_pieces_char:
        piece_name = PieceName(white_pieces_char.find(move[0]))
        move = move[1:]
    else:
        piece_name = PieceName.PAWN
    position_mapping = {position.name: position.value for position in Positions}
    target_square_str = move[-2:]
    if target_square_str in position_mapping.keys():
        target_square = Positions(position_mapping[target_square_str])
        move = move[:-2]
    if len(move) == 2:
        source_square_str = move
        if source_square_str in position_mapping.keys():
            source_square = Positions(position_mapping[source_square_str])
    elif len(move) == 1:
        if move.isdigit():
            source_file = move
        else:
            source_rank = move
    return PGNModel(piece_name=piece_name,
                    source_square=source_square,
                    source_file=source_file,
                    source_rank=source_rank,
                    target_square=target_square,
                    promotion_piece_name=promotion_piece_name,
                    capture_flag=capture_flag,
                    castle_flag=False)


def find_pgn_move_in_move_list(pgn_move: PGNModel, move_list: List[int]) -> int:
    for move in move_list:
        decrypted_move: Encryption = decode_move_all(move)
        if pgn_move.piece_name is decrypted_move.piece_name:
            source_square_matches: bool = pgn_move.source_square is decrypted_move.source_square
            if len(pgn_move.source_rank) != 0:
                source_square_matches = (pgn_move.source_rank == Positions.get_rank(
                    position=decrypted_move.source_square))
            elif len(pgn_move.source_file) != 0:
                source_square_matches = (pgn_move.source_file == Positions.get_file(
                    position=decrypted_move.source_square))
            if pgn_move.source_square is Positions.OUT_OF_BOUNDS and len(pgn_move.source_file) == 0 and len(
                    pgn_move.source_rank) == 0:
                source_square_matches = True
            target_square_matches: bool = pgn_move.target_square is decrypted_move.target_square
            promotion_piece_matches: bool = pgn_move.promotion_piece_name is decrypted_move.promotion_piece_name
            if source_square_matches and target_square_matches and promotion_piece_matches:
                return move
    return -1


def parse_pgn(pgn: str):
    pgn_list = pgn.split(' ')
    move_list = []
    for pgn_val in pgn_list:
        if '.' in pgn_val:
            move = pgn_val.split('.')[1]
        else:
            move = pgn_val
        move_list.append(move)
    return move_list


def find_move(move_list: List[int], pgn_move: PGNModel) -> int:
    for move in move_list:
        move_model: Encryption = decode_move_all(move=move)
        if move_model.piece_name is pgn_move.piece_name:
            if pgn_move.capture_flag and move_model.capture_flag:
                if pgn_move.source_square is move_model.source_square and pgn_move.target_square is move_model.target_square and move_model.piece_name is PieceName.KING:
                    return move
            if pgn_move.source_square is not Positions.OUT_OF_BOUNDS:
                if pgn_move.source_square is move_model.source_square and pgn_move.target_square is move_model.target_square:
                    if pgn_move.promotion_piece_name is not PieceName.NONE:
                        if pgn_move.promotion_piece_name is move_model.promotion_piece_name:
                            return move
                    else:
                        return move
    return 0
