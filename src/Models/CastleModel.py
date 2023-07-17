class Castle:
    def __init__(self, castle_rights: int):
        self.__castle_rights = castle_rights

    def can_castle(self) -> bool:
        return bool(self.__castle_rights)

    def can_queen_side_castle(self) -> bool:
        return bool(self.__castle_rights & 0b10)

    def can_king_side_castle(self) -> bool:
        return bool(self.__castle_rights & 0b1)

    def remove_king_side_rights(self):
        self.__castle_rights &= 0b0

    def remove_queen_side_rights(self):
        self.__castle_rights &= 0b10
