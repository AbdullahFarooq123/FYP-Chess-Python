from typing import List

from ChessEngine.src.Helpers.BeautifyHelpers.StringBeautifyHelpers import bool_to_str
from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Enums.PieceNameEnum import PieceName


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
    def get_str_attr() -> List[str]:
        return ['PIECE NAME', 'SOURCE SQ.', 'TARGET SQ.', 'DOUBLE PUSH', 'ENPASSANT', 'CAPTURE', 'CASTLE',
                'PROMOTION PIECE',
                'MOVE NAME']

    def get_value_list(self) -> List[str]:
        return [self.piece_name.name, self.source_square.name, self.target_square.name,
                bool_to_str(self.double_push_flag),
                bool_to_str(self.enpassant_flag),
                bool_to_str(self.capture_flag), bool_to_str(self.castle_flag), self.promotion_piece_name.name,
                self.get_move_name()]

    def get_move_name(self) -> str:
        from ChessEngine.src.Helpers.BeautifyHelpers.GameBeautifyHelpers import white_pieces_char
        move = ''
        if self.castle_flag:
            if self.target_square in [Positions.g1, Positions.g8]:
                move = 'O-O'
            elif self.target_square in [Positions.c1, Positions.c8]:
                move = 'O-O-O'
        else:
            if self.piece_name is not PieceName.PAWN:
                move += white_pieces_char[self.piece_name.value]
            move += self.source_square.name
            move += self.target_square.name
        return move
