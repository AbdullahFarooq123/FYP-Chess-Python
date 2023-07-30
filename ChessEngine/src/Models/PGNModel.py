from ChessEngine.src.Enums.PieceNameEnum import PieceName
from ChessEngine.src.Enums.PositionsEnum import Positions


class PGNModel:
    def __init__(self, piece_name: PieceName, source_square: Positions, source_file: str, source_rank: str,
                 target_square: Positions,
                 capture_flag: bool, castle_flag: bool, promotion_piece_name: PieceName):
        self.piece_name = piece_name
        self.source_square = source_square
        self.source_file = source_file
        self.source_rank = source_rank
        self.target_square = target_square
        self.capture_flag = capture_flag
        self.castle_flag = castle_flag
        self.promotion_piece_name = promotion_piece_name
