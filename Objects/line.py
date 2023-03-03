from ursina import Entity, Mesh
import Objects.controller as controller
from numpy import sqrt


def size_of_vec(vec):
    """
    Returns the size of a given vector
    :param vec: 3D vector
    :return: Size of 3D vector "vec"
    """
    return sqrt((vec.x ** 2 + vec.y ** 2 + vec.z ** 2))


def direction_cos(alpha, beta, gamma, vec):
    """
    Returns the directional cosine of 3 given angles: alpha, beta and gamma, compared to a given vector vec
    :param alpha: x-axis directional angle
    :param beta: y-axis directional angle
    :param gamma: z-axis directional angle
    :param vec: 3D vector
    :return: cos_alpha, cos_beta, cos_gamma, the 3 directional cosines
    """
    vec_size = size_of_vec(vec)
    cos_alpha = vec.x / vec_size
    cos_beta = vec.y / vec_size
    cos_gamma = vec.z / vec_size
    return cos_alpha, cos_beta, cos_gamma


class Line:
    def __init__(self, start, end, thickness, color):
        self.start = start
        self.end = end
        self.thickness = thickness
        self.color = color
        self.line_entity = controller.invoke_draw_line(self.start, self.end, self.thickness, self.color)
