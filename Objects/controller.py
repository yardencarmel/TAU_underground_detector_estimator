import View.viewer as viewer
import Objects.line as line
import Objects.Muon
from Objects.Muon import Muon
from Objects.Ground import Ground
import random as rnd
from Objects.scintillator import Scintillator
from ursina import Vec3, Vec2, color
from Model.rejection_sampling import RejectionSampling
import numpy as np
from Model.settings import SCINTILLATOR_SIZE_X, SCINTILLATOR_SIZE_Y, SCINTILLATOR_SIZE_Z, VEC0_3D, CREATION_HEIGHT, \
    GeV, MUON_COLOR, SCINTILLATOR_COLOR, GROUND_COLOR, WIRE_COLOR, m, CAVE_CEILING

objects = []
_rejection_sampling = RejectionSampling()


def invoke_draw_line(start, end, thickness, color):
    return viewer.draw_line(start, end, thickness, color)


def invoke_draw_cube(pos, size, mode, color):
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

    muons = []  # This hold the new n muons
    start_points = []  # This holds calculated start points
    curr_start_point = None  # This holds current start point of the muon in the iteration

    end_points = []  # This holds randomized end points
    curr_ent_point = None  # This holds current end point of the muon in the iteration

    # This holds the direction vectors between end point to start point: (sin(θ)*cos(φ), sin(θ)*sin(φ), cos(θ))
    direction_vectors = []

    # This holds tuples of (φ,θ) for each incident Muon. θ is the angle between the line to z axis
    angles = []
    phi = None
    theta = None

    # Check there exists a scintillator in the scene TODO: change when there are several scintillators
    scintillator_ref = [x for x in objects if isinstance(x, (Scintillator,))]  # Tries to get the scintillator obj
    if len(scintillator_ref) < 1:
        print("Please define a scintillator fist!")
        return
    scintillator_ref = scintillator_ref[0]  # the world's scintillator reference

    # For loop to create n muons
    for i in range(0, n):  # Create n end vectors for Muons
        # Randomize hit (end) point on the scintillator
        curr_ent_point = Vec3(rnd.uniform(scintillator_ref.pos.x - 0.5 * scintillator_ref.size.x,
                                          scintillator_ref.pos.x + 0.5 * scintillator_ref.size.x),
                              rnd.uniform(scintillator_ref.pos.y - 0.5 * scintillator_ref.size.y,
                                          scintillator_ref.pos.y + 0.5 * scintillator_ref.size.y),
                              round(scintillator_ref.pos.z + scintillator_ref.size.z / 2, 4))
        # Append the end point to a list for future use
        end_points.append(curr_ent_point)

        theta = _rejection_sampling.get_angles(1)[0]  # create randomized hit angles from cos^2 distribution
        # Randomize rotational angle for the incident muon
        phi = rnd.uniform(0, 2 * np.pi)
        angles.append((phi, theta))

        # Calculate the direction vector from end point to start point
        dx = np.sin(theta) * np.cos(phi)
        dy = np.sin(theta) * np.sin(phi)
        dz = np.cos(theta)
        curr_direction_vector = Vec3(dx, dy, dz)
        # Append the vector to the list of direction vectors
        direction_vectors.append(curr_direction_vector)

        # Declare the distance (length) of the total line path by CREATION_HEIGHT setting
        distance = CREATION_HEIGHT / np.cos(theta)

        # Calculate the start point by using linear line formula
        px = curr_ent_point.x + distance * curr_direction_vector.x
        py = curr_ent_point.y + distance * curr_direction_vector.y
        pz = curr_ent_point.z + distance * curr_direction_vector.z
        # Create a vector to the start point
        curr_start_point = Vec3(px, py, pz)
        # Append the start point's vector to a list of all start points
        start_points.append(curr_start_point)

        # Create a line based on the start point and end point, and create a muon obj based on that.
        line_i = invoke_draw_line(curr_start_point, curr_ent_point, 0.1, MUON_COLOR)
        muon_i = Muon(curr_start_point, curr_ent_point, 1 * GeV, line_i)
        add_to_objects_list(muon_i)
        muons.append(muon_i)
    return muons


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
    # scint_origin = VEC0_3D
    scint_rot = VEC0_3D  # in degrees
    cube = invoke_draw_cube(scint_pos, scint_size, 1, SCINTILLATOR_COLOR)
    wireframe = invoke_draw_cube(scint_pos, scint_size * 1.01, 0, color=WIRE_COLOR)
    scint = Scintillator(scint_pos, scint_size, scint_rot, cube, wireframe)

    objects.insert(-1, scint)  # TODO: understand if scintillator's size is from middle point or some edge point
    return scint


# def lists_to_vectors(end):
#     num_of_muons = len(end[0]) if (len(end[0]) == len(end[1]) == len(end[2])) else False
#     if not num_of_muons:
#         raise Exception("Number of end points not matching.")
#     end_vectors = []
#     for i in range(num_of_muons):
#         end_vector = Vec3(end[0][i], end[1][i], end[2][i])
#         end_vectors.append(end_vector)
#     return end_vectors


def create_ground(map_size, vacancy_pos, vacancy_size):  # TODO: understand the issue here
    ground_map = np.ones((map_size * m, map_size * m, map_size * m), dtype=float)
    ground_map[int(vacancy_pos.y):int(vacancy_pos.y + vacancy_size.y),
    int(vacancy_pos.x):int(vacancy_pos.x + vacancy_size.x),
    int(vacancy_pos.z):int(vacancy_pos.z + vacancy_size.z)] = np.zeros((int(vacancy_size.y), int(vacancy_size.x),
                                                                        int(vacancy_size.z)), dtype=int)
    X, Y, Z = ground_map.shape
    delta_x = -X / 2 + 0.5
    delta_y = -Y / 2 + 0.5
    for x in range(X):
        for y in range(Y):
            for z in range(Z):
                if ground_map[x][y][z]:
                    creat_ground_tile(Vec3(x + delta_x , y + delta_y, z+CAVE_CEILING))


def creat_ground_tile(pos, size=Vec3(1 * m, 1 * m, 1 * m)):
    cube = invoke_draw_cube(pos, size, 1, GROUND_COLOR)
    wireframe = invoke_draw_cube(pos, size * 1.01, 0, color=WIRE_COLOR)
    ground = Ground(pos, size, VEC0_3D, cube, wireframe)
    return ground
