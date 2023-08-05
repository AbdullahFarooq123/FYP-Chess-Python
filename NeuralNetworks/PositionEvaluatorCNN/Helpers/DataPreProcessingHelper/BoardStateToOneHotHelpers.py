from typing import Union

from pandas import Series



def get_feature_vector(fen: Union[str, Series]) -> List[int]:
    if type(fen) is Series and 'FEN' in fen:
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
