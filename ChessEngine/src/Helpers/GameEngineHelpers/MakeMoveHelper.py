from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Enums.PieceNameEnum import PieceName
from ChessEngine.src.Enums.PlayerSideEnum import PlayerSide
from ChessEngine.src.Models.EncryptionModel import Encryption
from ChessEngine.src.Helpers.MoveEncryptionHelpers.DecodeMoveHelpers import decode_move_all
from ChessEngine.src.Models.GameStateModel import GameState
from ChessEngine.src.Helpers.PreCalculationHelpers.BitManipulationHelpers import get_least_bit_index, remove_bit, \
    move_bit_by_position, add_bit
from ChessEngine.src.Root.PreCalculationsData import square_bitmask


def make_move(move: int, game_state_model: GameState):
    # Decode move
    decrypted_move: Encryption = decode_move_all(move=move)
    # Variables
    piece_to_move: PieceName = decrypted_move.piece_name
    player_pieces: list[int] = game_state_model.player_attr.player_pieces
    promotion_piece: PieceName = decrypted_move.promotion_piece_name
    piece_transform_to: PieceName = (promotion_piece if promotion_piece != PieceName.NONE else piece_to_move)

    # Perform move on board and player states
    __perform_movement_on_board_states(game_state_model=game_state_model, decrypted_moves=decrypted_move,
                                       piece_to_move=piece_to_move, piece_transform_to=piece_transform_to)

    __remove_castle_rights(game_state=game_state_model, decrypted_move=decrypted_move)

    # If there are any flags, make the moves, relative to the flag
    if decrypted_move.capture_flag or decrypted_move.enpassant_flag:
        __make_capture_move(game_state_model=game_state_model, decrypted_moves=decrypted_move)
    elif decrypted_move.double_push_flag:
        __make_double_push_move(game_state_model=game_state_model, decrypted_moves=decrypted_move)
    elif decrypted_move.castle_flag:
        __make_castle_move(game_state_model=game_state_model, decrypted_moves=decrypted_move)


    # Reset game state
    game_state_model.recalculate(change_turn=True)


def __make_capture_move(game_state_model: GameState, decrypted_moves: Encryption):
    # Variables
    target_position: Positions = decrypted_moves.target_square
    target_bitmask: int = square_bitmask[target_position.value]
    player_turn: PlayerSide = game_state_model.fen.player_turn
    opponent_state: int = game_state_model.fen.black_board if player_turn is PlayerSide.WHITE else game_state_model.fen.white_board
    opponent_pieces: list[
        int] = game_state_model.fen.black_pieces if player_turn is PlayerSide.WHITE else game_state_model.fen.white_pieces
    board_state: int = game_state_model.fen.game_board
    opponent_search_space: list[int] = opponent_pieces
    # For enpassant move (a type of capture move)
    if decrypted_moves.enpassant_flag:
        # If player side is white then the opponent will be located beneath the target square,
        # in other case above the target square. So we shift the bits of target position mask
        # by 8 depending on the player's turn (White or Black).
        opponent_piece_mask: int = target_bitmask >> 8 if player_turn is PlayerSide.WHITE else \
            target_bitmask << 8
        # If the move is enpassant then the target capture position is shifted 
        # according to the above calculation, and we get the position from the mask
        # by getting the least significant bit and converting to Positions. Least 
        # significant bit is actually the Index of least 1's bit.
        target_position = Positions(get_least_bit_index(opponent_piece_mask))
        # Enpassant is always performed on pawns. So reducing the search space to
        # pawns
        opponent_search_space = [opponent_pieces[PieceName.PAWN.value]]
        target_bitmask = opponent_piece_mask
        game_state_model.fen.game_board = remove_bit(board=board_state, position=target_position)

    # Remove the piece bit from the opponent's board state
    new_opponent_state = remove_bit(board=opponent_state, position=target_position)
    if player_turn is PlayerSide.WHITE:
        game_state_model.fen.black_board = new_opponent_state
    else:
        game_state_model.fen.white_board = new_opponent_state

    # Remove from the player piece's states
    for index, piece_state in enumerate(opponent_search_space):
        # Find the relevant opponent captured piece by taking
        # the calculated target mask's & with the piece state
        if piece_state & target_bitmask:
            # Remove the captured piece from that piece state
            opponent_pieces[index] = remove_bit(board=piece_state, position=target_position)
            break


def __make_double_push_move(game_state_model: GameState, decrypted_moves: Encryption):
    # Variables
    target_square_bitmask: int = square_bitmask[decrypted_moves.target_square.value]
    player_turn: PlayerSide = game_state_model.fen.player_turn

    # On double push, set the possible enpassant square. If the double push was
    # moved by the white then the enpassant square is just below the target square
    # otherwise above the target square. The target square bitmask is shifted by 8,
    # left or right, depending on the player's turn
    game_state_model.fen.enpassant_square_position = Positions(get_least_bit_index(target_square_bitmask << 8 if \
                                                                                       player_turn is not PlayerSide.WHITE \
                                                                                       else target_square_bitmask >> 8))


def __make_castle_move(game_state_model: GameState, decrypted_moves: Encryption):
    # Variables
    player_turn: PlayerSide = game_state_model.fen.player_turn
    castle_exists: bool = decrypted_moves.target_square in [Positions.g1, Positions.c1, Positions.g8, Positions.c8]
    king_target_square: Positions = decrypted_moves.target_square
    rook_state: int = game_state_model.player_attr.player_pieces[PieceName.ROOK.value]
    source_square: Positions = Positions.OUT_OF_BOUNDS
    target_square: Positions = Positions.OUT_OF_BOUNDS
    # Decide source square depending on the player's turn and revoke the
    # castle rights after that
    castle_moves = {
        (PlayerSide.WHITE, Positions.g1): (
            Positions.h1, Positions.f1, game_state_model.white_castle.remove_all_rights),
        (PlayerSide.WHITE, Positions.c1): (
            Positions.a1, Positions.d1, game_state_model.white_castle.remove_all_rights),
        (PlayerSide.BLACK, Positions.g8): (
            Positions.h8, Positions.f8, game_state_model.black_castle.remove_all_rights),
        (PlayerSide.BLACK, Positions.c8): (
            Positions.a8, Positions.d8, game_state_model.black_castle.remove_all_rights)
    }
    if (player_turn, king_target_square) in castle_moves:
        source_square, target_square, remove_relative_castle_rights = castle_moves[(player_turn, king_target_square)]
        remove_relative_castle_rights()

    # If castle move existed then change the states of the player and board
    if castle_exists:
        rook_decryption: Encryption = Encryption(piece_name=PieceName.ROOK,
                                                 source_square=source_square,
                                                 target_square=target_square,
                                                 promotion_piece_name=PieceName.NONE,
                                                 capture_flag=False,
                                                 double_push_flag=False,
                                                 enpassant_flag=False,
                                                 castle_flag=False)
        __perform_movement_on_board_states(game_state_model=game_state_model, decrypted_moves=rook_decryption,
                                           piece_to_move=PieceName.ROOK, piece_transform_to=PieceName.ROOK)


def __get_castle_bitmask_for_rook(target_square: Positions) -> int:
    # Get castle mask for rook based on king's target square
    rook_position: Positions = Positions.OUT_OF_BOUNDS
    if target_square is Positions.g1:
        rook_position = Positions.h1
    elif target_square is Positions.c1:
        rook_position = Positions.a1
    elif target_square is Positions.g8:
        rook_position = Positions.h8
    elif target_square is Positions.c8:
        rook_position = Positions.a8
    return square_bitmask[rook_position.value]


def __perform_movement_on_board_states(game_state_model: GameState, decrypted_moves: Encryption,
                                       piece_to_move: PieceName, piece_transform_to: PieceName):
    # Variables
    player_side: PlayerSide = game_state_model.player_attr.player_side
    player_state: int = game_state_model.fen.white_board if player_side is PlayerSide.WHITE else game_state_model.fen.black_board
    source_square: Positions = decrypted_moves.source_square
    target_square: Positions = decrypted_moves.target_square
    game_board: int = game_state_model.fen.game_board
    player_pieces: list[
        int] = game_state_model.fen.white_pieces if player_side is PlayerSide.WHITE else game_state_model.fen.black_pieces

    # Change player state
    player_state = move_bit_by_position(
        board=player_state,
        source_position=source_square,
        target_position=target_square)
    if player_side is PlayerSide.WHITE:
        game_state_model.fen.white_board = player_state
    else:
        game_state_model.fen.black_board = player_state

    # Removes a bit from player piece state
    player_pieces[piece_to_move.value] = remove_bit(
        board=player_pieces[piece_to_move.value],
        position=source_square)

    # Adds a bit to player piece state
    player_pieces[piece_transform_to.value] = add_bit(
        board=player_pieces[piece_transform_to.value],
        position=target_square)

    # Change game state
    game_state_model.fen.game_board = move_bit_by_position(board=game_board,
                                                           source_position=source_square,
                                                           target_position=target_square)


def __remove_castle_rights(game_state: GameState, decrypted_move: Encryption):
    piece_name: PieceName = decrypted_move.piece_name
    source_square: Positions = decrypted_move.source_square
    player_side: PlayerSide = game_state.player_attr.player_side
    if piece_name is PieceName.ROOK and source_square in [Positions.a8, Positions.h8, Positions.a1, Positions.h1]:
        if player_side is PlayerSide.WHITE:
            white_castle = game_state.white_castle
            if source_square is Positions.h1 and white_castle.can_king_side_castle():
                white_castle.remove_king_side_rights()
            elif source_square is Positions.a1 and white_castle.can_queen_side_castle():
                white_castle.remove_queen_side_rights()
        else:
            if source_square is Positions.h8 and game_state.black_castle.can_king_side_castle():
                game_state.black_castle.remove_king_side_rights()
            elif source_square is Positions.a8 and game_state.black_castle.can_queen_side_castle():
                game_state.black_castle.remove_queen_side_rights()
    elif piece_name is PieceName.KING:
        game_state.white_castle.remove_all_rights() if player_side is PlayerSide.WHITE else game_state.black_castle.remove_all_rights()
