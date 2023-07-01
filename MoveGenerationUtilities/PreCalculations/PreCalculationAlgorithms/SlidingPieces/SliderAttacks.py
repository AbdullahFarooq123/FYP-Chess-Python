from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Bishop import \
    get_bishop_magic_index_and_attack
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Rook import \
    get_rook_magic_index_and_attack
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import bishop_attacks_table


def init_slider_attacks(bishop: bool):
    for position in list(Positions)[:-1]:
        if bishop:
            for magic_index, attack in get_bishop_magic_index_and_attack(position=position):
                bishop_attacks_table[position.value][magic_index] = attack
        else:
            for magic_index, attack in get_rook_magic_index_and_attack(position=position):
                bishop_attacks_table[position.value][magic_index] = attack
