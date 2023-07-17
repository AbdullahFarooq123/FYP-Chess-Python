from src.Enums.DirectionsEnum import Direction


class RelativeDirection:
    def __init__(self, p1_position_wrt_p2: Direction, p2_position_wrt_p1: Direction):
        self.p1_position_wrt_p2 = p1_position_wrt_p2
        self.p2_position_wrt_p1 = p2_position_wrt_p1

    def is_aligned(self):
        return self.p1_position_wrt_p2 != Direction.NOT_ALIGNED and self.p2_position_wrt_p1 != Direction.NOT_ALIGNED

    def is_diagonal_aligned(self):
        return self.p1_position_wrt_p2 in list(Direction)[4:8]

    def is_horizontal_aligned(self):
        return self.p1_position_wrt_p2 in list(Direction)[0:4]
