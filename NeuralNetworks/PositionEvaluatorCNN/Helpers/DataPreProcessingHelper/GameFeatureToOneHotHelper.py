from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Root.PreCalculationsData import square_bitmask


def get_game_state_features(fen: str):
    _, player_turn, castle_rights, enpassant_square, half_move_clock, full_move = fen.split(' ')
    player_turn_features = get_player_turn_features(turn=player_turn)
    castle_rights_features = get_castle_rights_features(castle=castle_rights)
    enpassant_features = get_enpassant_square_features(enpassant_square=enpassant_square)
    half_move_features = [get_half_clock_move_features(moves=half_move_clock)]
    full_move_features = [get_full_move_features(moves=full_move)]
    return player_turn_features + castle_rights_features + enpassant_features + half_move_features + full_move_features


def get_player_turn_features(turn: str):
    return [1, 0] if 'w' == turn else [0, 1]


def get_castle_rights_features(castle: str):
    castle_rights = [0, 0, 0, 0]
    if '-' == castle:
        return castle_rights
    if 'K' in castle:
        castle_rights[0] = 1
    if 'Q' in castle:
        castle_rights[1] = 1
    if 'k' in castle:
        castle_rights[2] = 1
    if 'q' in castle:
        castle_rights[3] = 1
    return castle_rights


def get_half_clock_move_features(moves: str):
    moves: int = int(moves)
    return min_max_scale(moves, 0, 50)


def get_full_move_features(moves: str):
    moves: int = int(moves)
    return min_max_scale(moves, 1, 5899)


def min_max_scale(x: float, min_val: float, max_val: float):
    return (x - min_val) / (max_val - min_val)


def get_enpassant_square_features(enpassant_square: str):
    if '-' in enpassant_square:
        return [0 for _ in range(64)]
    enpassant_square_position = Positions.__members__[enpassant_square]
    bin_enc = square_bitmask[enpassant_square_position.value]
    return [int(_) for _ in '{:064b}'.format(bin_enc)]
