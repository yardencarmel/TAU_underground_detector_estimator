import random as rnd
import multiprocessing as mp
from numba import jit, cuda

import matplotlib.pyplot as plt
import numpy as np

import View.viewer as viewer
from Objects.Muon import Muon
from Objects.Ground import Ground
from Objects.scintillator import Scintillator
from Model.rejection_sampling import RejectionSampling
from Model.settings import *

objects = []
wireframes = []
ground_tiles = []
_rejection_sampling = RejectionSampling()
passed_muons = []
hits_on_scint_0 = []
hits_on_scint_1 = []
hits_on_scint_2 = []
hits_on_scint_3 = []
hits_on_scint_4 = []


def invoke_draw_line(start, end, thickness, color):
    return viewer.draw_line(start, end, thickness, color)


def invoke_draw_cube(pos, size, color):
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
    curr_end_point = None  # This holds current end point of the muon in the iteration

    # This holds the direction vectors between end point to start point: (sin(θ)*cos(φ), sin(θ)*sin(φ), cos(θ))
    direction_vectors = []

    # This holds tuples of (φ,θ) for each incident Muon. θ is the angle between the line to z axis
    angles = []
    phi = None
    theta = None
    theta = _rejection_sampling.get_angles(n)

    # Check there exists a scintillator in the scene TODO: change when there are several scintillators
    scintillator_ref = [x for x in objects if isinstance(x, (Scintillator,))]  # Tries to get the scintillator obj
    if len(scintillator_ref) < 1:
        print("Please define a scintillator fist!")
        return
    scintillator_ref = scintillator_ref[0]  # the world's scintillator reference

    # For loop to create n muons
    for i in range(0, n):  # Create n end vectors for Muons
        # Randomize hit (end) point on the scintillator
        curr_end_point = Vec3(rnd.uniform(scintillator_ref.pos.x - 0.5 * scintillator_ref.size.x,
                                          scintillator_ref.pos.x + 0.5 * scintillator_ref.size.x),
                              rnd.uniform(scintillator_ref.pos.y - 0.5 * scintillator_ref.size.y,
                                          scintillator_ref.pos.y + 0.5 * scintillator_ref.size.y),
                              round(
                                  scintillator_ref.pos.z - NUMBER_OF_SCINTS * SCINTILLATOR_SPACING + scintillator_ref.size.z / 2,
                                  4))
        # Append the end point to a list for future use
        end_points.append(curr_end_point)

        # theta = _rejection_sampling.get_angles(1)[0]  # create randomized hit angles from cos^2 distribution
        curr_theta = theta[i]
        # Randomize rotational angle for the incident muon
        phi = rnd.uniform(0, 2 * np.pi)
        angles.append((phi, curr_theta))

        # Calculate the direction vector from end point to start point
        dx = np.sin(curr_theta) * np.cos(phi)
        dy = np.sin(curr_theta) * np.sin(phi)
        dz = np.cos(curr_theta)
        curr_direction_vector = Vec3(dx, dy, dz)
        # Append the vector to the list of direction vectors
        direction_vectors.append(curr_direction_vector)

        # Declare the distance (length) of the total line path by CREATION_HEIGHT setting
        distance = CREATION_HEIGHT / np.cos(curr_theta)

        # Calculate the start point by using linear line formula
        px = curr_end_point.x + distance * curr_direction_vector.x
        py = curr_end_point.y + distance * curr_direction_vector.y
        pz = curr_end_point.z + distance * curr_direction_vector.z
        # Create a vector to the start point
        curr_start_point = Vec3(px, py, pz)
        # Append the start point's vector to a list of all start points
        start_points.append(curr_start_point)

        # Create a line based on the start point and end point, and create a muon obj based on that.
        # line_i = None  # Do not draw muons
        # if i % 1 == 0:
        #     line_i = invoke_draw_line(curr_start_point, curr_end_point, 0.1, MUON_COLOR)
        line_i = invoke_draw_line(curr_start_point, curr_end_point, 0.1, MUON_COLOR) #None  #
        muon_i = Muon(i, curr_start_point, curr_end_point, 1 * GeV, line_i)
        add_to_objects_list(muon_i)
        muons.append(muon_i)
    return muons


def create_scintillator(num_of_scints):
    """
    This function will create the main scintillator 
    :return: Returns the scintillator object
    """""
    NUMBER_OF_SCINTS = num_of_scints
    scintillator_ref = [x for x in objects if isinstance(Scintillator, x)]
    if len(scintillator_ref) > 0:
        print("A scintillator is already defined!")
        return
    scint_size = Vec3(SCINTILLATOR_SIZE_X, SCINTILLATOR_SIZE_Y, SCINTILLATOR_SIZE_Z)  # set in settings
    scint_rot = VEC0_3D  # in degrees
    for i in range(num_of_scints):
        scint_pos = Vec3(0, 0, -num_of_scints / 2 + 0.5) * 0.1 + Vec3(0, 0, 1) * 0.1 * i  # in meters
        wireframe = invoke_draw_cube(scint_pos, scint_size * 1.01, color=WIRE_COLOR)
        scint = Scintillator(i, scint_pos, scint_size, scint_rot, wireframe)
        wireframe.collider = None
        wireframe.parent = scint
    # scint_origin = VEC0_3D
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


def create_ground(map_size, vacancy_pos, vacancy_size):
    ground_map = np.ones((int(map_size.x), int(map_size.y), int(map_size.z)), dtype=int)

    ground_map[int(vacancy_pos.x):int(vacancy_pos.y + vacancy_size.x),
    int(vacancy_pos.y):int(vacancy_pos.x + vacancy_size.y),
    int(vacancy_pos.z):int(vacancy_pos.z + vacancy_size.z)] = \
        np.zeros((int(vacancy_size.y), int(vacancy_size.x), int(vacancy_size.z)), dtype=int)

    X, Y, Z = ground_map.shape
    delta_x = -X / 2 + 0.5
    delta_y = -Y / 2 + 0.5
    for x in range(X):
        for y in range(Y):
            for z in range(Z):
                if ground_map[x][y][z]:
                    curr_ground = creat_ground_tile(Vec3(x + delta_x, y + delta_y, GROUND_SLATE_Z * z + CAVE_CEILING))
                    add_to_objects_list(curr_ground)


# TODO: understand how to create ground tile that inherits from cube
def creat_ground_tile(pos, size=Vec3(GROUND_SLATE_X, GROUND_SLATE_Y, GROUND_SLATE_Z)):
    cube = invoke_draw_cube(pos, size, 1, GROUND_COLOR)
    cube.collider = 'box'
    wireframe = invoke_draw_cube(pos, size * 1.01, 0, color=WIRE_COLOR)
    wireframes.append(wireframe)
    ground = Ground(pos, size, VEC0_3D, cube, wireframe, cube.collider)
    ground_tiles.append(ground)
    return ground


def worker(muon):
    return muon.calculate_collisions()


def check_muons_collisions(muons):
    # processes = 4
    scint0, scint1, scint2, scint3, scint4 = None #  TODO: FINISH IT
    # p = processes(Muon.calculate_collisions())
    # pool = mp.Pool(mp.cpu_count() - 1)
    # pool.map(worker, muons)
    # pool.close()
    # pool.join()
    hit_entities = []

    for muon in muons:
        # if muon.index % 100 == 0:
        #     print("Checked collision on " + str(muon.index) + " muons.")
        scint0, scint1, scint2, scint3, scint4 = muon.calculate_collisions()
        hits_on_scint_0 += scint0
    for i in range(NUMBER_OF_SCINTS):
        if i == 0:
            create_hits_hist(hits_on_scint_0, 25, i)
        if i == 1:
            create_hits_hist(hits_on_scint_1, 25, i)
        if i == 2:
            create_hits_hist(hits_on_scint_2, 25, i)
        if i == 3:
            create_hits_hist(hits_on_scint_3, 25, i)
        if i == 4:
            create_hits_hist(hits_on_scint_4, 25, i)

    num_muons_passed = len(passed_muons)
    print("Passed muons: " + str(num_muons_passed) + " = " + str(100 * num_muons_passed / NUMBER_OF_MUONS) + "%")
    return hit_entities


def create_hits_hist(hit_points, bins, index):
    # for hit_point in hit_points:
    x = np.array([hit_point.x for hit_point in hit_points])
    y = np.array([hit_point.y for hit_point in hit_points])
    plt.hist2d(x, y, bins=bins)
    plt.title("Hits Histogram for Scint Index " + str(index) + ", bins=" + str(bins))
    plt.colorbar()
    plt.show()


def create_start_hist(start_points, bins):
    x = [start_point_x.x for start_point_x in start_points]
    y = [start_point_y.y for start_point_y in start_points]
    plt.hist2d(x, y, bins=bins, range=[[-10, 10], [-10, 10]])
    plt.title("Starts Histogram, bins=" + str(bins))
    plt.colorbar()
    plt.show()


def test_rej(n):
    plt.figure()
    theta = []
    for i in range(n):
        theta.append(_rejection_sampling.get_angles(1)[0])
    plt.hist(theta, bins=100, alpha=0.1)
    plt.show()
