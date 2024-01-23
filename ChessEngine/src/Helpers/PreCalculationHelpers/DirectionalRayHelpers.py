from ChessEngine.src.Enums.DirectionsEnum import \
    Direction
from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Helpers.PreCalculationHelpers.BitManipulationHelpers import move_bit_by_position, \
    move_bit_by_direction
from ChessEngine.src.Root.PreCalculationsData import square_bitmask


def init_directional_rays():
    directional_rays = [0 for _ in list(Direction)[:8]]
    for direction in list(Direction)[:8]:
        directional_rays[direction.value] = get_all_uni_directional_rays(direction)
    return directional_rays, 'directional_rays'


def get_all_uni_directional_rays(direction: Direction):
    uni_directional_ray_list = [0 for _ in range(64)]
    for position in list(Positions)[:-1]:
        uni_directional_ray_list[position.value] = get_ray_wrt_pos_dir(direction, position)
    return uni_directional_ray_list


def get_ray_wrt_pos_dir(direction: Direction, position: Positions):
    my_position = square_bitmask[position.value]
    ray = 0
    while my_position:
        my_position = move_bit_by_direction(my_position, direction)
        ray |= my_position
    return ray
