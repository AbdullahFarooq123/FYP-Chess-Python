from pandas import Series

from ChessEngine.src.Enums.PieceNameEnum import PieceName
from ChessEngine.src.Enums.PlayerSideEnum import PlayerSide
from ChessEngine.src.Helpers.FenHelpers.FenDecryptHelpers import decrypt_fen
from ChessEngine.src.Helpers.MoveGenerationHelpers.OpponentMoveHelpers import get_opponent_attacks_and_find_check
from ChessEngine.src.Models.AttackOnKingModel import AttackOnKing
from ChessEngine.src.Models.CastleModel import Castle
from ChessEngine.src.Models.FenModel import Fen
from ChessEngine.src.Models.PlayerModel import Player


def fen_to_one_hot(fen: str | Series):
    if type(fen) is Series:
        fen = fen['FEN']
    board_state = fen.split(' ')[0]
    one_hot_dict = {'.': 0,
                    'p': 1,
                    'n': 2,
                    'b': 4,
                    'r': 8,
                    'q': 16,
                    'k': 32,
                    'P': 64,
                    'N': 128,
                    'B': 256,
                    'R': 512,
                    'Q': 1024,
                    'K': 2048}
    board_state: str = board_state.replace('/', '')
    board_state: str = ''.join('.' * int(char) if char.isdigit() else char for char in board_state)
    return [convert_to_bin_array(one_hot_dict[square]) for square in board_state]


def convert_to_bin_array(number: int):
    return [int(_) for _ in '{:012b}'.format(number)]


def extract_player_features(fen: str):
    pad: list[int] = [0 for _ in range(6)]
    fen: Fen = decrypt_fen(fen=fen)
    white_castle: Castle = Castle(castle_rights=fen.white_castle)
    black_castle: Castle = Castle(castle_rights=fen.black_castle)
    white_king_side_castle: int = int(white_castle.can_king_side_castle())
    white_queen_side_castle: int = int(white_castle.can_queen_side_castle())
    black_king_side_castle: int = int(black_castle.can_king_side_castle())
    black_queen_side_castle: int = int(black_castle.can_queen_side_castle())
    current_player: Player = fen.get_current_player()
    opponent_player: Player = fen.get_opponent_player()
    attack_on_king_attr: AttackOnKing = get_opponent_attacks_and_find_check(
        opponent_pieces=opponent_player.player_pieces,
        player_king_mask=current_player.get_piece_mask(PieceName.KING), opponent_side=opponent_player.name,
        board_state=fen.game_board,
        player_king_position=current_player.get_piece_position(PieceName.KING))
    white_in_check: int = int(fen.player_turn is PlayerSide.WHITE and attack_on_king_attr.check_count > 0)
    black_in_check: int = int(fen.player_turn is PlayerSide.BLACK and attack_on_king_attr.check_count > 0)
    white_features: list[int] = [white_king_side_castle, white_queen_side_castle, white_in_check]
    black_features: list[int] = [black_king_side_castle, black_queen_side_castle, black_in_check]
    return white_features + black_features + pad
