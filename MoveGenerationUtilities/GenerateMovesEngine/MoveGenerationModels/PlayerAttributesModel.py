from DebugUtilities.GameDependency.PlayerDependency.PlayerSideDependency import PlayerSide


class PlayerAttribute:
    def __init__(self, player_pieces: list, player_side: PlayerSide, opponent_pieces: list, opponent_side: PlayerSide):
        self.player_pieces = player_pieces
        self.player_side = player_side
        self.opponent_pieces = opponent_pieces
        self.opponent_side = opponent_side
