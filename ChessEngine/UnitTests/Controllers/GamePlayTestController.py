from ChessEngine.UnitTests.Helpers.GamePlayTestHelper import get_test_games
from ChessEngine.src.Helpers.BeautifyHelpers.GameBeautifyHelpers import print_moves, print_game_board, get_binary
from ChessEngine.src.Helpers.FenHelpers.FenDecryptHelpers import decrypt_fen
from ChessEngine.src.Helpers.FenHelpers.FenEncryptHelpers import encrypt_fen
from ChessEngine.src.Helpers.GameEngineHelpers.MakeMoveHelper import make_move
from ChessEngine.src.Helpers.PGNHelpers.ParseMoveHelper import parse_user_move, find_pgn_move_in_move_list
from ChessEngine.src.Models.FenModel import Fen
from ChessEngine.src.Models.GameStateModel import GameState
from ChessEngine.src.Models.PGNModel import PGNModel


def run_game_play_tests():
    castles = {
        'WHITE': {
            'O-O-O': False,
            'O-O': False
        },
        'BLACK': {
            'O-O-O': False,
            'O-O': False
        }
    }
    games: list[dict] = get_test_games()
    count: int = 1
    for game in games:
        print(f'Game {count} started')
        fen: Fen = decrypt_fen(Fen.start_position)
        # print_game_board(fen)
        game_state: GameState = GameState(fen)
        for pgn_test_move in game['Game']:
            if pgn_test_move in castles[game_state.player_attr.player_side.name]:
                castles[pgn_test_move] = True
            # print(f'{game_state.player_attr.player_side.name} s Turn.')
            pgn_move: PGNModel = parse_user_move(move=pgn_test_move, player_turn=game_state.player_attr.player_side)
            move = find_pgn_move_in_move_list(pgn_move=pgn_move, move_list=game_state.moves)
            if True in castles[game_state.player_attr.player_side.name].values():
                print(game_state.white_castle.can_castle())
                print(game_state.black_castle.can_castle())
                input()
            if pgn_test_move in [''] and game['Details']['Date'] == '2006.03.09':
                print(encrypt_fen(game_state.fen))
                print_moves(game_state.moves)
            if move != -1:
                make_move(move, game_state)
                # print(f'Move : {pgn_test_move}')
                # print_game_board(game_state.fen)
                # print(f'Black Rights : {get_binary(game_state.black_castle.castle_rights)}')
                # print(f'White Rights : {get_binary(game_state.white_castle.castle_rights)}')
            else:
                print(f'Details : {game["Details"]}')
                print(encrypt_fen(game_state.fen))
                print(f'Move {pgn_test_move} not found in game {count}!')
                print_moves(game_state.moves)
                print_game_board(game_state.fen)
                print(get_binary(game_state.black_castle.castle_rights))
                input()
        print(f'Game {count} completed!')
        count += 1
