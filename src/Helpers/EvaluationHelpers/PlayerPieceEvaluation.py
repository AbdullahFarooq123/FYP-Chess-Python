from src.Enums.PieceNameEnum import PieceName
from src.Helpers.PreCalculationHelpers.BitManipulationHelpers import count_set_bits
from src.Root.Const import piece_scores


def get_piece_score(piece_list: list[int]) -> int:
    player_piece_score = 0
    for piece_name in list(PieceName)[:-1]:
        player_piece_bitmask = piece_list[piece_name.value]
        piece_count = count_set_bits(player_piece_bitmask)
        player_piece_score += (piece_scores[piece_count] * piece_count)
    return player_piece_score
