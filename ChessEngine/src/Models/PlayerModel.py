from typing import List

from ChessEngine.src.Enums.PieceNameEnum import PieceName
from ChessEngine.src.Enums.PlayerSideEnum import PlayerSide
from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Helpers.PreCalculationHelpers.BitManipulationHelpers import get_least_bit_index
from ChessEngine.src.Models.CastleModel import Castle


class Player:
    def __init__(self, player_pieces: List[int], player_board: int, castle_rights: Castle, my_turn: bool,
                 name: PlayerSide):
        self.player_pieces: List[int] = player_pieces
        self.player_board: int = player_board
        self.castle_rights: Castle = castle_rights
        self.my_turn: bool = my_turn
        self.name: PlayerSide = name

    def get_piece_mask(self, piece_name: PieceName) -> int:
        return self.player_pieces[piece_name.value]

    def get_piece_position(self, piece_name: PieceName) -> Positions:
        return Positions(get_least_bit_index(self.player_pieces[piece_name.value]))
