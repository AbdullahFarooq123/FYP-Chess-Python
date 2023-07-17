import os

from stockfish import Stockfish

from src.Models.FenModel import Fen


class StockFishEngine:
    def __init__(self):
        params = {
            'UCI_Elo': 4000,
            'Threads': 4,
            'Hash': 8192
        }
        self.stock_fish = Stockfish(path=f'{os.getcwd()}\\stockfish\\stockfish-windows-x86-64-avx2.exe',
                                    parameters=params)
