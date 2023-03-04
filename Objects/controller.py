import View.viewer as viewer
import Objects.line as line
import Objects.Muon
from Objects.Muon import Muon
import random as rnd
from Objects.scintillator import Scintillator
from ursina import Vec3, Vec2
from Model.rejection_sampling import RejectionSampling
import numpy as np
from Model.settings import SCINTILLATOR_SIZE_X, SCINTILLATOR_SIZE_Y, SCINTILLATOR_SIZE_Z, VEC0_3D, CREATION_HEIGHT, \
    GeV, MUON_COLOR, SCINTILLATOR_COLOR

objects = []
_rejection_sampling = RejectionSampling()


def invoke_draw_line(start, end, thickness, color):
    return viewer.draw_line(start, end, thickness, color)


def invoke_draw_cube(pos, size, mode, color=SCINTILLATOR_COLOR):
    if mode: return viewer.draw_cube(pos, size, color)
    return viewer.draw_wireframe_cube(pos, size, color)


def add_to_objects_list(_object):
    objects.append(_object)
    return _object


def create_n_random_muons(n):
    """
    This function will create and print n muons of varying energies and angels
    :param n: Number of muons
    :return: Array of all muons
    """

    # this holds the direction angle alpha/beta (between x/y-axis and end point) for each end point
    direction_angles = []

    directions_vectors = []  # holds directions vectors from end to future start points:
    # (cos(α)*sin(θ)*cos(β) + sin(α)*sin(θ)*sin(β), sin(α)*sin(θ)*cos(β) - cos(α)*sin(θ)*sin(*β), cos θ)

    unit_directions_vectors = []  # holds unit directions vectors from end to future start points

    distances = []  # holds the distances between end points to start points

    start_points = []

    scintillator_ref = [x for x in objects if isinstance(x, (Scintillator,))]
    if len(scintillator_ref) < 1:
        print("Please define a scintillator fist!")
        return

    scintillator_ref = scintillator_ref[0]  # the world's scintillator reference
    end_point = None
    for i in range(1, n + 1):  # Create n end vectors for Muons
        end_point = Vec3(rnd.uniform(scintillator_ref.pos.x - 0.5 * scintillator_ref.size.x,
                                     scintillator_ref.pos.x + 0.5 * scintillator_ref.size.x),
                         rnd.uniform(scintillator_ref.pos.y - 0.5 * scintillator_ref.size.y,
                                     scintillator_ref.pos.y + 0.5 * scintillator_ref.size.y),
                         round(scintillator_ref.pos.z + scintillator_ref.size.z / 2, 4))

        # end_point_vector = Vec3(*end_point)
        incident_angle = _rejection_sampling.get_angles(1)[0]  # create randomized hit angles from cos^2 distribution

        _direction_angles = line.direction_angles(end_point)
        #direction_angles.append(_direction_angles)  # calculate the direction angles from each end point
        cos_direction_x = np.cos(_direction_angles.x)  # calculate cos(a) for each
        sin_direction_x = np.sin(_direction_angles.x)  # calculate sin(a) for each
        cos_direction_y = np.cos(_direction_angles.y)
        sin_direction_y = np.sin(_direction_angles.y)
        direction_vector = Vec3(
            np.sin(incident_angle) * (cos_direction_x * cos_direction_y + sin_direction_x * sin_direction_y),
            np.sin(incident_angle) * (sin_direction_x * cos_direction_y - cos_direction_x * sin_direction_y),
            np.cos(incident_angle))
        distances = CREATION_HEIGHT / np.cos(incident_angle)

        size_of_vec = line.size_of_vec(direction_vector)
        x_val = direction_vector.x / size_of_vec
        y_val = direction_vector.y / size_of_vec
        z_val = direction_vector.z / size_of_vec
        unit_directions_vectors.append(Vec3(x_val, y_val, z_val))

        start_x = end_point.x + distances * unit_directions_vectors[i].x
        start_y = end_point.y + distances * unit_directions_vectors[i].y
        start_z = end_point.z + distances * unit_directions_vectors[i].z
        start_points.append(Vec3(start_x, start_y, start_z))

        line_i = invoke_draw_line(start_points[i], end_point_vector, 1, MUON_COLOR)
        muon_i = Muon(start_points[i], end_point_vector, 1 * GeV, line_i)

    # for i in range(1, n + 1):  # Create n end vectors for Muons
    #     end_points = [[rnd.uniform(scintillator_ref.pos.x - 0.5*scintillator_ref.size.x,
    #                                scintillator_ref.pos.x + 0.5*scintillator_ref.size.x) for k in np.ones((n,),
    #                                                                                                       dtype=int)],
    #                   [rnd.uniform(scintillator_ref.pos.y - 0.5*scintillator_ref.size.y,
    #                                scintillator_ref.pos.y + 0.5*scintillator_ref.size.y) for l in np.ones((n,),
    #                                                                                                       dtype=int)],
    #                   [round(scintillator_ref.pos.z + scintillator_ref.size.z / 2, 4) for m in
    #                    np.ones((n,), dtype=int)]]
    #
    # end_points = lists_to_vectors(end_points)  # convert the end points to a list of 3D vectors instead of list of lists
    #
    # incident_angles = _rejection_sampling.get_angles(n)  # create randomized hit angles from cos^2 distribution
    #
    # for end_point, angle in zip(end_points, incident_angles):
    #     _direction_angles = line.direction_angles(end_point)
    #     direction_angles.append(_direction_angles)  # calculate the direction angles from each end point
    #     cos_direction_x = np.cos(_direction_angles.x)  # calculate cos(a) for each
    #     sin_direction_x = np.sin(_direction_angles.x)  # calculate sin(a) for each
    #     cos_direction_y = np.cos(_direction_angles.y)
    #     sin_direction_y = np.sin(_direction_angles.y)
    #     directions_vectors.append(Vec3(
    #         np.sin(angle)*(cos_direction_x * cos_direction_y + sin_direction_x * sin_direction_y),
    #         np.sin(angle)*(sin_direction_x * cos_direction_y - cos_direction_x * sin_direction_y),
    #         np.cos(angle)))
    #     distances.append(CREATION_HEIGHT / np.cos(angle))
    #
    # for direction_vector in directions_vectors:
    #     size_of_vec = line.size_of_vec(direction_vector)
    #     x_val = direction_vector.x / size_of_vec
    #     y_val = direction_vector.y / size_of_vec
    #     z_val = direction_vector.z / size_of_vec
    #     unit_directions_vectors.append(Vec3(x_val, y_val, z_val))
    #
    # for i in range(len(end_points)):
    #     start_x = end_points[i].x + distances[i] * unit_directions_vectors[i].x
    #     start_y = end_points[i].y + distances[i] * unit_directions_vectors[i].y
    #     start_z = end_points[i].z + distances[i] * unit_directions_vectors[i].z
    #     start_points.append(Vec3(start_x, start_y, start_z))
    #
    # for i in range(n):
    #     line_i = invoke_draw_line(start_points[i],end_points[i],1,MUON_COLOR)
    #     muon_i = Muon(start_points[i], end_points[i], 1 * GeV, line_i)  # TODO: randomize locations and momentas.


def create_scintillator():
    """
    This function will create the main scintillator 
    :return: Returns the scintillator object
    """""
    scintillator_ref = [x for x in objects if isinstance(Scintillator, x)]
    if len(scintillator_ref) > 0:
        print("A scintillator is already defined!")
        return
    scint_size = Vec3(SCINTILLATOR_SIZE_X, SCINTILLATOR_SIZE_Y, SCINTILLATOR_SIZE_Z)  # set in settings
    scint_pos = VEC0_3D  # in meters
    scint_origin = VEC0_3D
    scint_rot = VEC0_3D  # in degrees
    cube = invoke_draw_cube(scint_pos, scint_size, 1)
    wireframe = invoke_draw_cube(scint_pos, scint_size, 0)
    scint = Scintillator(scint_pos, scint_size, scint_rot, cube, wireframe)

    objects.insert(-1, scint)  # TODO: understand if scintillator's size is from middle point or some edge point
    return scint


def lists_to_vectors(end):
    num_of_muons = len(end[0]) if (len(end[0]) == len(end[1]) == len(end[2])) else False
    if not num_of_muons:
        raise Exception("Number of end points not matching.")
    end_vectors = []
    for i in range(num_of_muons):
        end_vector = Vec3(end[0][i], end[1][i], end[2][i])
        end_vectors.append(end_vector)
    return end_vectors
