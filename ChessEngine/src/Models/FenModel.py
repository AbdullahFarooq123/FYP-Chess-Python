from ChessEngine.src.Enums.PlayerSideEnum import PlayerSide
from ChessEngine.src.Models.CastleModel import Castle
from ChessEngine.src.Models.PlayerModel import Player


class Fen:
    start_position = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

    def __init__(self, game_board, player_turn, white_pieces, white_board, white_castle, black_pieces, black_board,
                 black_castle, enpassant_square_position):
        self.game_board = game_board
        self.player_turn = player_turn
        self.white_pieces = white_pieces
        self.white_board = white_board
        self.white_castle = white_castle
        self.black_pieces = black_pieces
        self.black_board = black_board
        self.black_castle = black_castle
        self.enpassant_square_position = enpassant_square_position

    def get_opponent_player(self) -> Player:
        return Player(
            player_pieces=self.black_pieces if self.player_turn is PlayerSide.WHITE else self.white_pieces,
            player_board=self.black_board if self.player_turn is PlayerSide.WHITE else self.white_board,
            castle_rights=Castle(
                castle_rights=(self.black_castle if self.player_turn is PlayerSide.WHITE else self.white_castle)),
            my_turn=False,
            name=PlayerSide.BLACK if self.player_turn is PlayerSide.WHITE else PlayerSide.WHITE
        )

    def get_current_player(self) -> Player:
        return Player(
            player_pieces=self.white_pieces if self.player_turn is PlayerSide.WHITE else self.black_pieces,
            player_board=self.white_board if self.player_turn is PlayerSide.WHITE else self.black_board,
            castle_rights=Castle(
                castle_rights=(self.white_castle if self.player_turn is PlayerSide.WHITE else self.black_castle)),
            my_turn=True,
            name=self.player_turn
        )
