from ursina import Entity, Mesh, Vec3
import Objects.controller as controller
from numpy import sqrt
from numpy import arccos
from Model.VectorCalculations import size_of_vec


# def direction_angles(vec):
#     """
#     Returns the directional cosine of 3 given of a given vector vec
#     :param vec: 3D vector
#     :return: cos_alpha, cos_beta, cos_gamma, the 3 directional cosines
#     """
#     vec_size = size_of_vec(vec)
#     alpha = arccos(vec.x / vec_size)
#     beta = arccos(vec.y / vec_size)
#     gamma = arccos(vec.z / vec_size)
#
#     return Vec3(alpha, beta, gamma)


class Line:
    def __init__(self, start, end, thickness, color):
        self.start = start
        self.end = end
        self.thickness = thickness
        self.color = color
        self.line_entity = controller.invoke_draw_line(self.start, self.end, self.thickness, self.color)
