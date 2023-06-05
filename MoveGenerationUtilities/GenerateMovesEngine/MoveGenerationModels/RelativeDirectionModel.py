from DebugUtilities.GameDependency.BoardDependency.DirectionalDependency.SpecificDirectionDependency import \
    SpecificDirections


class RelativeDirection:
    def __init__(self, p1_position_wrt_p2: SpecificDirections, p2_position_wrt_p1: SpecificDirections):
        self.p1_position_wrt_p2 = p1_position_wrt_p2
        self.p2_position_wrt_p1 = p2_position_wrt_p1

    def is_aligned(self):
        return self.p1_position_wrt_p2 != SpecificDirections.NOT_ALIGNED and self.p2_position_wrt_p1 != SpecificDirections.NOT_ALIGNED

    def is_diagonal_aligned(self):
        return self.p1_position_wrt_p2 in list(SpecificDirections)[4:8]

    def is_horizontal_aligned(self):
        return self.p1_position_wrt_p2 in list(SpecificDirections)[0:4]
