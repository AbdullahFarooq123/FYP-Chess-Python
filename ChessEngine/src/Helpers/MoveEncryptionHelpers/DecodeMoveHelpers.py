from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Enums.PieceNameEnum import PieceName
from ChessEngine.src.Models.EncryptionModel import Encryption
from ChessEngine.src.Enums.MoveEncryptionEnum import \
    MoveEncryptionAttributes, EncryptionPrams


def decode_move(move: int, attribute_name: MoveEncryptionAttributes) -> int:
    return int(move >> attribute_name.value[EncryptionPrams.SHIFT_BITS.value]) \
        & int(attribute_name.value[EncryptionPrams.SET_BITS.value])


def decode_move_all(move: int) -> Encryption:
    piece_name: PieceName = PieceName(decode_move(move, MoveEncryptionAttributes.PIECE_NAME))
    source_square: Positions = Positions(decode_move(move, MoveEncryptionAttributes.SOURCE_SQUARE))
    target_square: Positions = Positions(decode_move(move, MoveEncryptionAttributes.TARGET_SQUARE))
    promotion_piece_name: PieceName = PieceName(decode_move(move, MoveEncryptionAttributes.PROMOTION_PIECE_NAME))
    capture_flag: bool = bool(decode_move(move, MoveEncryptionAttributes.CAPTURE_FLAG))
    double_push_flag: bool = bool(decode_move(move, MoveEncryptionAttributes.DOUBLE_PUSH_FLAG))
    enpassant_flag: bool = bool(decode_move(move, MoveEncryptionAttributes.EN_PASSANT_FLAG))
    castle_flag: bool = bool(decode_move(move, MoveEncryptionAttributes.CASTLE_FLAG))
    return Encryption(piece_name=piece_name, source_square=source_square, target_square=target_square,
                      promotion_piece_name=promotion_piece_name, capture_flag=capture_flag,
                      double_push_flag=double_push_flag,
                      enpassant_flag=enpassant_flag, castle_flag=castle_flag)
