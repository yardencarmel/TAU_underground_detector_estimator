import numpy as np
def size_of_vec(vec):
    """
    Returns the size of a given vector
    :param vec: 3D vector
    :return: Size of 3D vector "vec"
    """
    return np.sqrt((vec.x ** 2 + vec.y ** 2 + vec.z ** 2))

def calculate_direction_between_points(p1,p2):
    direction = (p1-p2)/size_of_vec(p1-p2)
    return direction