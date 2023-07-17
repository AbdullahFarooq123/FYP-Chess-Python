import os
import time

from NeuralNetworks.StockFish import StockFishEngine
from UnitTests.Enums.TestOfEnum import TestsOf
from src.Controllers import PreCalculationsController
from src.Helpers.FenHelpers.FenDecryptHelpers import decrypt_fen
from src.Controllers.GenerateMovesController import get_moves_by_fen

from UnitTests.Controllers.UnitTestController import UnitTestEngine
from src.Helpers.BeautifyHelpers.GameBeautifyHelpers import print_moves, print_fen_board, print_game_board
from src.Helpers.FenHelpers.FenEncryptHelpers import encrypt_fen
from src.Helpers.PreCalculationHelpers.BitManipulationHelpers import unsigned, count_set_bits
from src.Models.FenModel import Fen


def run_unit_test():
    u_engine = UnitTestEngine(show_only_tests=TestsOf.FAILED, print_test_cases=TestsOf.FAILED,
                              print_test_case_details=TestsOf.FAILED)
    u_engine.run_tests()
    u_engine.print_tests()


def run_migrations():
    PreCalculationsController.init_migrations()


def run_testing():
    print(Fen.start_position)
    fen = decrypt_fen(Fen.start_position)
    print(encrypt_fen(fen))


if __name__ == '__main__':
    run_testing()
    # run_unit_test()
    # run_migrations()
