from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Helpers.PreCalculationHelpers.BishopPreCalHelpers import \
    get_bishop_magic_index_and_attack
from ChessEngine.src.Helpers.PreCalculationHelpers.RookPreCalHelpers import \
    get_rook_magic_index_and_attack


def init_slider_attacks(bishop: bool):
    bishop_attacks_table = [[0 for _ in range(4096)] for _ in list(Positions)[:-1]]
    rook_attacks_table = [[0 for _ in range(4096)] for _ in list(Positions)[:-1]]
    for position in list(Positions)[:-1]:
        if bishop:
            for magic_index, attack in get_bishop_magic_index_and_attack(position=position):
                bishop_attacks_table[position.value][magic_index] = attack
        else:
            for magic_index, attack in get_rook_magic_index_and_attack(position=position):
                rook_attacks_table[position.value][magic_index] = attack
    return [bishop_attacks_table, 'bishop_attacks_table'] if bishop else [rook_attacks_table, 'rook_attacks_table']
