from src.Enums.PositionsEnum import Positions
from src.Enums.PieceNameEnum import PieceName
from src.Helpers.PreCalculationHelpers.BitManipulationHelpers import unsigned


#   castle   enpassant   double push  Capture  Promotion piece  piece_name   Target sq  Source sq
#     0          0             0         0          0000           0000       000000     000000
def encode_move(source_square: Positions, target_square: Positions, piece_name: PieceName,
                promotion_piece_name: PieceName, capture_flag: bool,
                double_push_flag: bool, enpassant_flag: bool, castle_flag: bool):
    return unsigned(source_square.value) | \
           unsigned(target_square.value << 6) | \
           unsigned(piece_name.value << 12) | \
           unsigned(promotion_piece_name.value << 16) | \
           unsigned(capture_flag << 20) | \
           unsigned(double_push_flag << 21) | \
           unsigned(enpassant_flag << 22) | \
           unsigned(castle_flag << 23)
