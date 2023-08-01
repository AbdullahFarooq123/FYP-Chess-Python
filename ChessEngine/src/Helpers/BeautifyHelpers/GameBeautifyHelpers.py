import numpy as numpy
from typing import List

from ChessEngine.src.Helpers.BeautifyHelpers.StringBeautifyHelpers import print_by_padding, pad_str_list
from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Models.EncryptionModel import Encryption
from ChessEngine.src.Helpers.MoveEncryptionHelpers.DecodeMoveHelpers import decode_move_all
from ChessEngine.src.Models.FenModel import Fen
from ChessEngine.src.Root.PreCalculationsData import square_bitmask

white_pieces_char = 'PNBRQK'
black_pieces_char = 'pnbrqk'
files = 'abcdefgh'


def print_bitboard(bit_board: int):
    bin_val = get_binary(bit_board)
    for file in range(8):
        print(8 - file, end='\t')
        for rank in range(8):
            print(bin_val[file * 8 + rank], end='  ')
        print()
    __print_files()


def get_binary(number: int, start='', end='') -> str:
    return start + '{:064b}'.format(number) + end


def __print_files():
    print('\n\t', end='')
    for file in files:
        print(file, end='  ')
    print()


def print_moves(move_list: list):
    if len(move_list) == 0:
        return
    str_length = 198
    print_by_padding('', str_length - 8)
    print_by_padding('', str_length - 8, start_end_only=True)
    print_by_padding('MOVES TABLE', str_length - 8, start_end_only=True)
    print_by_padding('', str_length - 8, start_end_only=True)
    print_by_padding('', str_length - 8)
    print(pad_str_list(Encryption.get_str_attr(), total_length=str_length))
    print_by_padding('', str_length - 8)
    for move in move_list:
        encryption: Encryption = decode_move_all(move)
        print(pad_str_list(encryption.get_value_list(), str_length))
    print_by_padding('', str_length - 8)


def print_game_board(fen: Fen):
    white_pieces = numpy.array(fen.white_pieces, dtype=numpy.uint64)
    black_pieces = numpy.array(fen.black_pieces, dtype=numpy.uint64)
    for file in range(7, -1, -1):
        print(file+1, end='\t')
        for rank in range(7, -1, -1):
            current_square_mask = square_bitmask[file * 8 + rank]
            if current_square_mask & fen.white_board:
                print(white_pieces_char[int((white_pieces & current_square_mask).nonzero()[0])], end='  ')
            elif current_square_mask & fen.black_board:
                print(black_pieces_char[int((black_pieces & current_square_mask).nonzero()[0])], end='  ')
            else:
                print('.', end='  ')
        print()
    __print_files()


def print_fen_board(fen: str):
    fen = fen.split(' ')[0]
    index = 8
    print(index, end='\t')
    for char in fen:
        if char == '/':
            print()
            index -= 1
            print(index, end='\t')
        elif char.isdigit():
            for i in range(int(char)):
                print('.', end='  ')
        else:
            print(char, end='  ')
    __print_files()


def print_attack_map(attack_map: List[int]):
    for position in reversed(list(Positions)[:-1]):
        print(f'\'{position.name}\':')
        print('\'\'\'')
        binary = get_binary(attack_map[position.value])
        for index, bit in enumerate(binary):
            if index != 0 and index % 8 == 0:
                print()
            print(bit, end=' ')
        print()
        print('\'\'\',')
