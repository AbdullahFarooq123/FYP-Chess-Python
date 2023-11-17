from ChessEngine.src.Enums.PieceNameEnum import PieceName
from ChessEngine.src.Enums.PlayerSideEnum import PlayerSide
from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Helpers.BeautifyHelpers.GameBeautifyHelpers import black_pieces_char, white_pieces_char
from ChessEngine.src.Models.FenModel import Fen
from ChessEngine.src.Root.PreCalculationsData import square_bitmask


def encrypt_fen(fen: Fen):
    fen_string = __get_piece_string(fen) + ' '
    fen_string += __get_player_side(fen) + ' '
    fen_string += __get_castle_rights(fen) + ' '
    fen_string += __get_enpassant(fen) + ' 0 0'
    return fen_string


def __get_piece_string(fen: Fen):
    space_count = 0
    char_count = 0
    fen_string = ''
    for position in list(Positions)[:-1]:
        position_mask = square_bitmask[position.value]
        if fen.game_board & position_mask:
            if space_count != 0:
                fen_string += f'{space_count}'
            white_piece = bool(fen.white_board & position_mask)
            player_pieces = fen.white_pieces if white_piece else fen.black_pieces
            ascii_char = white_pieces_char if white_piece else black_pieces_char
            for piece_name in list(PieceName)[:-1]:
                if player_pieces[piece_name.value] & position_mask:
                    fen_string += ascii_char[piece_name.value]
                    space_count = 0
                    break
        else:
            space_count += 1
        char_count += 1
        if char_count % 8 == 0 and char_count != 64:
            if space_count != 0:
                fen_string += f'{space_count}'
                space_count = 0
            fen_string += '/'
    if space_count!=0:
        fen_string += f'{space_count}'
    return fen_string


def __get_player_side(fen: Fen):
    return 'w' if fen.player_turn is PlayerSide.WHITE else 'b'


def __get_castle_rights(fen: Fen):
    castle_rights = ''
    castle_char = ['', 'K', 'Q', 'KQ']
    castle_rights += castle_char[fen.white_castle]
    castle_rights += castle_char[fen.black_castle].lower()
    if len(castle_rights) == 0:
        castle_rights = '-'
    return castle_rights


def __get_enpassant(fen: Fen):
    if fen.enpassant_square_position is Positions.OUT_OF_BOUNDS:
        return '-'
    return fen.enpassant_square_position.name
