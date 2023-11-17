from ChessEngine.src.Enums.MoveEncryptionEnum import \
    MoveEncryptionAttributes
from ChessEngine.src.Helpers.MoveEncryptionHelpers.EncodeMoveHelpers import encode_move


def encrypt_move(json_encrypted: dict) -> int:
    return encode_move(
        source_square=json_encrypted[MoveEncryptionAttributes.SOURCE_SQUARE.name],
        target_square=json_encrypted[MoveEncryptionAttributes.TARGET_SQUARE.name],
        piece_name=json_encrypted[MoveEncryptionAttributes.PIECE_NAME.name],
        promotion_piece_name=json_encrypted[MoveEncryptionAttributes.PROMOTION_PIECE_NAME.name],
        capture_flag=json_encrypted[MoveEncryptionAttributes.CAPTURE_FLAG.name],
        double_push_flag=json_encrypted[MoveEncryptionAttributes.DOUBLE_PUSH_FLAG.name],
        enpassant_flag=json_encrypted[MoveEncryptionAttributes.EN_PASSANT_FLAG.name],
        castle_flag=json_encrypted[MoveEncryptionAttributes.CASTLE_FLAG.name]
    )
