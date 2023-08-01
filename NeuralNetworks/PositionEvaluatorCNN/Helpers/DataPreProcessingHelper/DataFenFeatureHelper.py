from typing import Union, List, Tuple

from pandas import Series

from ChessEngine.src.Enums.PieceNameEnum import PieceName
from ChessEngine.src.Enums.PlayerSideEnum import PlayerSide
from ChessEngine.src.Helpers.FenHelpers.FenDecryptHelpers import decrypt_fen
from ChessEngine.src.Helpers.MoveGenerationHelpers.OpponentMoveHelpers import get_opponent_attacks_and_find_check
from ChessEngine.src.Models.AttackOnKingModel import AttackOnKing
from ChessEngine.src.Models.CastleModel import Castle
from ChessEngine.src.Models.FenModel import Fen
from ChessEngine.src.Models.PlayerModel import Player


def get_feature_vector(fen: Union[str, Series]) -> List[int]:
    if type(fen) is Series and 'FEN' in fen:
        fen = fen['FEN']
    eval_fen: str = fen
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
    white_features: List[int] = [white_king_side_castle, white_queen_side_castle, white_in_check]
    black_features: List[int] = [black_king_side_castle, black_queen_side_castle, black_in_check]
    eval_fen: Tuple[int] = fen_to_eval(str_fen=eval_fen)
    lst_eval: List[int] = list(eval_fen)
    # if fen.player_turn is PlayerSide.BLACK:
    #     lst_eval: list[int] = [elem * -1 for elem in lst_eval[::-1]]
    #     white_features, black_features = black_features, white_features
    input_features = white_features + black_features + lst_eval
    return input_features


def fen_to_eval(str_fen: str) -> Tuple[int]:
    str_fen = str_fen.split(' ')[0]
    str_fen = ''.join(',0' * int(char) if char.isdigit() else char for char in str_fen)
    str_fen = str_fen.replace('/', '')
    str_fen = str_fen.replace("p", ",-1")
    str_fen = str_fen.replace("n", ",-3")
    str_fen = str_fen.replace("b", ",-4")
    str_fen = str_fen.replace("r", ",-5")
    str_fen = str_fen.replace("q", ",-9")
    str_fen = str_fen.replace("k", ",-100")
    str_fen = str_fen.replace("P", ",1")
    str_fen = str_fen.replace("N", ",3")
    str_fen = str_fen.replace("B", ",4")
    str_fen = str_fen.replace("R", ",5")
    str_fen = str_fen.replace("Q", ",9")
    str_fen = str_fen.replace("K", ",100")
    str_fen = str_fen[1:]
    str_fen = eval(str_fen)
    return str_fen
