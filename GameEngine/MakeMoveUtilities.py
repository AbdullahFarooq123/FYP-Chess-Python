from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from DebugUtilities.GameDependency.PieceDependency.PieceNameDependency import PieceName
from DebugUtilities.GameDependency.PlayerDependency.PlayerSideDependency import PlayerSide
from MoveGenerationUtilities.EncryptionDependency.EncryptionModels.EncryptionModel import Encryption
from MoveGenerationUtilities.EncryptionDependency.MoveEncryptions.DecodeMove import decode_move_all
from MoveGenerationUtilities.GenerateMovesEngine.MoveGenerationModels.MovesModel import GameStateModel
from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import unsigned, get_least_bit_index
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import square_bitmask


def make_move(move: int, game_state_model: GameStateModel):
    # Decode move
    decrypted_moves: Encryption = decode_move_all(move=move)

    # Variables
    piece_to_move: PieceName = decrypted_moves.piece_name
    player_pieces: list[int] = game_state_model.player_attr.player_pieces
    player_piece_state: int = player_pieces[piece_to_move.value]
    promotion_piece: PieceName = decrypted_moves.promotion_piece_name
    piece_transform_to: PieceName = (promotion_piece if promotion_piece != PieceName.NONE else piece_to_move)
    transformed_piece_state: int = player_pieces[piece_transform_to.value]

    # Set board and player states
    __perform_movement_on_board_states(game_state_model=game_state_model, decrypted_moves=decrypted_moves,
                                       piece_to_move=piece_to_move, piece_transform_to=piece_transform_to,
                                       player_piece_state=player_piece_state,
                                       transformed_piece_state=transformed_piece_state)

    # If there are any flags, make the moves, relative to the flag
    if decrypted_moves.capture_flag or decrypted_moves.enpassant_flag:
        __make_capture_move(game_state_model=game_state_model, decrypted_moves=decrypted_moves)
    elif decrypted_moves.double_push_flag:
        __make_double_push_move(game_state_model=game_state_model, decrypted_moves=decrypted_moves)
    elif decrypted_moves.castle_flag:
        __make_castle_move(game_state_model=game_state_model, decrypted_moves=decrypted_moves)

    # Reset game state
    game_state_model.recalculate(change_turn=True)


def move_bit(board: int, source_position: Positions, target_position: Positions) -> int:
    board = remove_bit(board, source_position)
    board = add_bit(board, target_position)
    return board


def remove_bit(board: int, position: Positions):
    return board & unsigned(~square_bitmask[position.value])


def add_bit(board: int, position: Positions):
    return board | square_bitmask[position.value]


def __make_capture_move(game_state_model: GameStateModel, decrypted_moves: Encryption):
    # Variables
    target_position: Positions = decrypted_moves.target_square
    target_bitmask: int = square_bitmask[target_position.value]
    player_turn: PlayerSide = game_state_model.fen.player_turn
    opponent_state: int = game_state_model.player_attr.opponent_state
    opponent_pieces: list[int] = game_state_model.player_attr.opponent_pieces

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
        opponent_pieces = opponent_pieces[PieceName.PAWN.value]

    # Remove the piece bit from the opponent's board state
    game_state_model.player_attr.opponent_state = remove_bit(board=opponent_state, position=target_position)

    # Remove from the player piece's states
    for index, piece_state in enumerate(opponent_pieces):
        # Find the relevant opponent captured piece by taking
        # the calculated target mask's & with the piece state
        if piece_state & target_bitmask:
            # Remove the captured piece from that piece state
            game_state_model.player_attr.opponent_pieces[index] = remove_bit(board=piece_state,
                                                                             position=target_position)
            break


def __make_double_push_move(game_state_model: GameStateModel, decrypted_moves: Encryption):
    # Variables
    target_square_bitmask: int = square_bitmask[decrypted_moves.target_square.value]
    player_turn: PlayerSide = game_state_model.fen.player_turn

    # On double push, set the possible enpassant square. If the double push was
    # moved by the white then the enpassant square is just below the target square
    # otherwise above the target square. The target square bitmask is shifted by 8,
    # left or right, depending on the player's turn
    game_state_model.fen.enpassant_square_position = target_square_bitmask << 8 if \
        player_turn is PlayerSide.WHITE \
        else target_square_bitmask >> 8


def __make_castle_move(game_state_model: GameStateModel, decrypted_moves: Encryption):
    # Variables
    player_turn: PlayerSide = game_state_model.fen.player_turn
    castle_exists: bool = decrypted_moves.target_square in [Positions.g1, Positions.c1, Positions.g8, Positions.c8]
    king_target_square: Positions = decrypted_moves.target_square
    rook_state: int = game_state_model.player_attr.player_pieces[PieceName.ROOK.value]

    # Decide source square depending on the player's turn and revoke the
    # castle rights after that
    castle_moves = {
        (PlayerSide.WHITE, Positions.g1): (Positions.h1, game_state_model.white_castle.remove_king_side_rights),
        (PlayerSide.WHITE, Positions.c1): (Positions.a1, game_state_model.white_castle.remove_queen_side_rights),
        (PlayerSide.BLACK, Positions.g8): (Positions.h8, game_state_model.black_castle.remove_king_side_rights),
        (PlayerSide.BLACK, Positions.c8): (Positions.a8, game_state_model.black_castle.remove_queen_side_rights)
    }
    if (player_turn, king_target_square) in castle_moves:
        source_square, remove_relative_castle_rights = castle_moves[(player_turn, king_target_square)]
        remove_relative_castle_rights()

    # If castle move existed then change the states of the player and board
    if castle_exists:
        __perform_movement_on_board_states(game_state_model=game_state_model, decrypted_moves=decrypted_moves,
                                           piece_to_move=PieceName.ROOK, piece_transform_to=PieceName.ROOK,
                                           player_piece_state=rook_state, transformed_piece_state=rook_state)


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


def __perform_movement_on_board_states(game_state_model: GameStateModel, decrypted_moves: Encryption,
                                       piece_to_move: PieceName, piece_transform_to: PieceName, player_piece_state: int,
                                       transformed_piece_state: int):
    # Variables
    player_state: int = game_state_model.player_attr.player_state
    source_square: Positions = decrypted_moves.source_square
    target_square: Positions = decrypted_moves.target_square
    game_board: int = game_state_model.fen.game_board

    # Change player state
    game_state_model.player_attr.player_state = move_bit(board=player_state,
                                                         source_position=source_square,
                                                         target_position=target_square)

    # Removes a bit from player piece state
    game_state_model.player_attr.player_pieces[piece_to_move.value] = remove_bit(
        board=player_piece_state,
        position=source_square)

    # Adds a bit to player piece state
    game_state_model.player_attr.player_pieces[piece_transform_to.value] = add_bit(
        board=transformed_piece_state,
        position=target_square)

    # Change game state
    game_state_model.fen.game_board = move_bit(board=game_board,
                                               source_position=source_square,
                                               target_position=target_square)
