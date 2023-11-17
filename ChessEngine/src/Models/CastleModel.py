class Castle:
    def __init__(self, castle_rights: int):
        self.castle_rights = castle_rights

    def can_castle(self) -> bool:
        return bool(self.castle_rights)

    def can_queen_side_castle(self) -> bool:
        return bool(self.castle_rights & 0b10)

    def can_king_side_castle(self) -> bool:
        return bool(self.castle_rights & 0b01)

    def remove_king_side_rights(self):
        self.castle_rights &= 0b10

    def remove_queen_side_rights(self):
        self.castle_rights &= 0b01

    def remove_all_rights(self):
        self.castle_rights = 0
