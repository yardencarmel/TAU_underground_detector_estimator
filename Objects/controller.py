import View.viewer as viewer
import Objects.line as line
import Objects.Muon
from Objects.Muon import Muon
import random as rnd
from Objects.scintillator import Scintillator
from ursina import Vec3
from Model.rejection_sampling import RejectionSampling
import numpy as np
from Model.settings import SCINTILLATOR_SIZE_X, SCINTILLATOR_SIZE_Y, SCINTILLATOR_SIZE_Z, VEC0_3D


objects = []
_rejection_sampling = RejectionSampling()


def invoke_draw_line(start, end, thickness, color):
    return viewer.draw_line(start, end, thickness, color)


def add_to_objects_list(_object):
    objects.append(_object)
    return _object



def create_n_random_muons(n):
    """
    This function will create and print n muons of varying energies and angels
    :param n: Number of muons
    :return: Array of all muons
    """
    scintillator_ref = [x for x in objects if isinstance(x, (Scintillator,))]
    if len(scintillator_ref) < 1:
        print("Please define a scintillator fist!")
        return

    scintillator_ref = scintillator_ref[0] # the world's scintillator reference

    for i in range(1, n + 1):  # Create n end vectors for Muons
        # Creates Muons' end points to be traced back to starting point
        end_points = [[rnd.uniform(scintillator_ref.pos.x - scintillator_ref.size.x,
                            scintillator_ref.pos.x + scintillator_ref.size.x) for i in np.ones((n,), dtype=int)],
               [rnd.uniform(scintillator_ref.pos.y - scintillator_ref.size.y,
                            scintillator_ref.pos.y + scintillator_ref.size.y) for j in np.ones((n,), dtype=int)],
               [round(scintillator_ref.pos.z + scintillator_ref.size.z / 2, 4) for k in np.ones((n,), dtype=int)]]
    end_points = lists_to_vectors(end_points) # convert the end points to a list of 3D vectors instead of list of lists

    direction_angles = [] # this holds the direction angles (alpha) for each end point

    incident_angles = _rejection_sampling.get_angles(n) # create randomized hit angles from cos^2 distribution

    directions_vectors = [] # holds directions vectors from
                            # end to future start points (cos α sin θ, sin α sin θ, cos θ)


    for end_point, angle in zip(end_points, incident_angles):
        direction_angles.append(line.direction_angles(end_point)) # calculate the direction angles from each end point
        cos_direct_x = np.cos(direction_angles[end_point][0]) # calculate cos(θ) for each
        directions_vectors.append(Vec3(cos_direct_x * np.sin(angle)))

    for
    # start # TODO: Calculate start point by end point and distance
    # TODO: Enter angel from cos^2 and trace back the starting point.
    muon_i = Muon()  # TODO: randomize locations and momentas.


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

    scint = Scintillator(scint_pos, scint_size, scint_rot)

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