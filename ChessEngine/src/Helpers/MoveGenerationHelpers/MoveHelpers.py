from typing import List

from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Enums.PieceNameEnum import PieceName
from ChessEngine.src.Enums.PlayerSideEnum import PlayerSide
from ChessEngine.src.Enums.MoveEncryptionEnum import \
    MoveEncryptionAttributes
from ChessEngine.src.Helpers.MoveEncryptionHelpers.DecodeMoveHelpers import decode_move
from ChessEngine.src.Models.PlayerAttributesModel import PlayerAttribute


def get_sliding_pieces(piece_list: list) -> int:
    return piece_list[PieceName.BISHOP.value] | piece_list[PieceName.ROOK.value] | \
        piece_list[PieceName.QUEEN.value]


def get_sliding_pieces_list(piece_list: list) -> List[int]:
    return [piece_list[PieceName.BISHOP.value], piece_list[PieceName.ROOK.value],
            piece_list[PieceName.QUEEN.value]]


def get_player_wise_pieces_and_sides(white_pieces: list, white_state: int, black_pieces: list, black_state: int,
                                     turn: PlayerSide) -> PlayerAttribute:
    return PlayerAttribute(player_pieces=black_pieces, player_state=black_state, player_side=PlayerSide.BLACK,
                           opponent_pieces=white_pieces, opponent_state=white_state,
                           opponent_side=PlayerSide.WHITE) if turn == PlayerSide.BLACK else PlayerAttribute(
        player_pieces=white_pieces, player_state=white_state, player_side=PlayerSide.WHITE,
        opponent_pieces=black_pieces, opponent_state=black_state,
        opponent_side=PlayerSide.BLACK)


def get_enpassant_move(enpassant_square: Positions, previous_move: int) -> Positions:
    if enpassant_square != Positions.OUT_OF_BOUNDS:
        return enpassant_square
    if decode_move(previous_move, MoveEncryptionAttributes.DOUBLE_PUSH_FLAG):
        source_square = decode_move(previous_move, MoveEncryptionAttributes.SOURCE_SQUARE)
        target_square = decode_move(previous_move, MoveEncryptionAttributes.TARGET_SQUARE)
        return Positions((source_square + target_square) / 2)
    return Positions.OUT_OF_BOUNDS
