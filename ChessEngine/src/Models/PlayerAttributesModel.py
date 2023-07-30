from ChessEngine.src.Enums.PlayerSideEnum import PlayerSide


class PlayerAttribute:
    def __init__(self, player_pieces: list, player_state: int, player_side: PlayerSide, opponent_pieces: list,
                 opponent_state: int, opponent_side: PlayerSide):
        self.player_state = player_state
        self.player_pieces = player_pieces
        self.player_side = player_side
        self.opponent_state = opponent_state
        self.opponent_pieces = opponent_pieces
        self.opponent_side = opponent_side
