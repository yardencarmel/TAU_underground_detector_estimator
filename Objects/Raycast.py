from ursina import Vec3
from Model.VectorCalculations import size_of_vec


def calculate_raycast_direction(start, end):
    vec = start - end
    direction = vec / size_of_vec(vec)
    return direction
