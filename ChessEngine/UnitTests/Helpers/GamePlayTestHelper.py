import os
import re


def get_test_games() -> list[dict]:
    pgn_data: str = __load_pgn()
    games: list[dict] = __parse_pgn(pgn_data)
    return games


def __load_pgn() -> str:
    file_path: str = f'{os.getcwd()}\\UnitTests\\TestData\\Nakamura.pgn'
    try:
        with open(file_path, 'r') as game_pgn:
            return game_pgn.read()
    except FileNotFoundError:
        return ''


def __parse_pgn(pgn_str: str) -> list[dict]:
    regular_exp: str = r'\[[^\]]*\]'
    games: list[dict] = []
    # pgn_str: str = re.sub(regular_exp, '', pgn_str)
    pgn_list: list[str] = pgn_str.split('\n')
    end_games: list[str] = ['1-0', '0-1', '1/2-1/2']
    single_game: list[str] = []
    details: dict = {}
    for pgn_line in pgn_list:
        if len(pgn_line) == 0:
            continue
        if '[' in pgn_line:
            pgn_line = pgn_line.replace('[', '').replace(']', '')
            details_line = pgn_line.split('"')
            details[details_line[0].strip()] = details_line[1].strip()
            continue
        moves: list[str] = pgn_line.split(' ')
        for move in moves:
            if len(move) == 0:
                continue
            if '.' in move:
                valid_move = move.split('.')[1]
            else:
                valid_move = move
            if valid_move in end_games:
                games.append({
                    'Details': details,
                    'Game': single_game
                })
                single_game = []
                details = {}
            else:
                single_game.append(valid_move.strip())
    return games
