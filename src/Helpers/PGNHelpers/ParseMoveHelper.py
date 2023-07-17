import re

from src.Helpers.BeautifyHelpers.GameBeautifyHelpers import white_pieces_char
from src.Enums.PositionsEnum import Positions
from src.Enums.PieceNameEnum import PieceName
from src.Enums.PlayerSideEnum import PlayerSide
from src.Models.EncryptionModel import Encryption
from src.Helpers.MoveEncryptionHelpers.DecodeMoveHelpers import decode_move_all
from src.Models.PGNModel import PGNModel


def parse_user_move(move: str, player_turn: PlayerSide) -> PGNModel | None:
    piece_name: PieceName = PieceName.NONE
    source_square: Positions = Positions.OUT_OF_BOUNDS
    target_square: Positions = Positions.OUT_OF_BOUNDS
    capture_flag: bool = 'x' in move
    source_file = ''
    move = re.sub(r'[x#+]|1-0|0-1|0-0', '', move)
    if len(move) == 0:
        return None
    index_of_promotion_piece_name = move.find('=')
    promotion_piece_ascii = '' if index_of_promotion_piece_name == -1 else white_pieces_char[
        move[index_of_promotion_piece_name + 1]]
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
                        source_file='',
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
        source_file = move
    return PGNModel(piece_name=piece_name,
                    source_square=source_square,
                    source_file=source_file,
                    target_square=target_square,
                    promotion_piece_name=promotion_piece_name,
                    capture_flag=capture_flag,
                    castle_flag=False)


def parse_pgn(pgn: str):
    pgn_list = pgn.split(' ')
    move_list = []
    for pgn_val in pgn_list:
        move = ''
        if '.' in pgn_val:
            move = pgn_val.split('.')[1]
        else:
            move = pgn_val
        move_list.append(move)
    return move_list


def find_move(move_list: list[int], pgn_move: PGNModel) -> int:
    for move in move_list:
        move_model: Encryption = decode_move_all(move=move)
        if move_model.piece_name is pgn_move.piece_name:
            is_found = False
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
