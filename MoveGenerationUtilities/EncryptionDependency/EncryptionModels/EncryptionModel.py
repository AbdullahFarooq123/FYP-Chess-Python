from DebugUtilities.BeautifyDependency.StringBeautify import bool_to_str
from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from DebugUtilities.GameDependency.PieceDependency.PieceNameDependency import PieceName


class Encryption:
    def __init__(self, piece_name: PieceName, source_square: Positions, target_square: Positions,
                 promotion_piece_name: PieceName, capture_flag: bool, double_push_flag: bool, enpassant_flag: bool,
                 castle_flag: bool):
        self.piece_name = piece_name
        self.source_square = source_square
        self.target_square = target_square
        self.promotion_piece_name = promotion_piece_name
        self.capture_flag = capture_flag
        self.double_push_flag = double_push_flag
        self.enpassant_flag = enpassant_flag
        self.castle_flag = castle_flag

    @staticmethod
    def get_str_attr() -> list[str]:
        return ['PIECE NAME', 'SOURCE SQ.', 'TARGET SQ.', 'DOUBLE PUSH', 'ENPASSANT', 'CAPTURE', 'CASTLE',
                'PROMOTION PIECE',
                'MOVE NAME']

    def get_value_list(self) -> list[str]:
        return [self.piece_name.name, self.source_square.name, self.target_square.name,
                bool_to_str(self.double_push_flag),
                bool_to_str(self.enpassant_flag),
                bool_to_str(self.capture_flag), bool_to_str(self.castle_flag), self.promotion_piece_name.name, '']
