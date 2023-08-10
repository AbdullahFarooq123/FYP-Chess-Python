import csv
import os

import chess
import chess.pgn
import sys

import numpy
from pandas import DataFrame

pgnfilename = 'D:\\FYP_Chess_Python\\pgn_files'
dirs = os.listdir(pgnfilename)
count = len(dirs)
# Open the PGN file and read the gam
for dir in dirs[212:1244]:
    # Open the PGN file and read the games
    win_games = []
    with open(pgnfilename + "\\" + dir) as pgn_file:
        while True:
            try:
                game = chess.pgn.read_game(pgn_file)
            except UnicodeDecodeError:
                continue
            if game is None:
                break

            # Play through the moves and find the end of the game
            board = game.board()
            for move in game.mainline_moves():
                board.push(move)

            # Print the FEN of the endgame position

            if board.is_checkmate():
                endgame_fen = board.fen()
                score = 10000 * (-1 if 'w' in endgame_fen else 1)
                win_games.append([str(endgame_fen), score])

    # print(win_games)

    with open("Checkmates.csv", mode='a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for item in win_games:
            if isinstance(item, list):
                csv_writer.writerow(item)
            else:
                csv_writer.writerow([item])

    print("Remaining : " + str(count))
    count -= 1
