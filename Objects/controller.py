import View.viewer as viewer
import Objects.line
import Objects.Muon
from Objects.Muon import Muon
import random as rnd
from Objects.scintillator import Scintillator
from ursina import Vec3
from Model.rejection_sampling import RejectionSampling
import numpy as np

objects = []
_rejection_sampling = RejectionSampling()

from Model.settings import SCINTILLATOR_SIZE_X, SCINTILLATOR_SIZE_Y, SCINTILLATOR_SIZE_Z, VEC0_3D


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

    scintillator_ref = scintillator_ref[0]

    for i in range(1, n + 1):
        end = [[rnd.uniform(scintillator_ref.pos.x-scintillator_ref.size.x,
                            scintillator_ref.pos.x+scintillator_ref.size.x) for i in np.ones((n,), dtype=int)],
               [rnd.uniform(scintillator_ref.pos.y-scintillator_ref.size.y,
                            scintillator_ref.pos.y+scintillator_ref.size.y) for j in np.ones((n,), dtype=int)]]
        angles = _rejection_sampling.get_angles(n)
        start # TODO: Calculate start point by end point and distance
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
