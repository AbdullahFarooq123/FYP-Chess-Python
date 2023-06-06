from DebugUtilities.GameDependency.PlayerDependency.PlayerSideDependency import PlayerSide


class Castle:
    def __init__(self, castle_rights: int):
        self.__castle_rights = castle_rights

    def can_castle(self) -> bool:
        return bool(self.__castle_rights)

    def can_queen_side_castle(self) -> bool:
        return bool(self.__castle_rights & 0b10)

    def can_king_side_castle(self) -> bool:
        return bool(self.__castle_rights & 0b1)

