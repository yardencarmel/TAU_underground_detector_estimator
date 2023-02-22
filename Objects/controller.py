import View.viewer as viewer
import Objects.line
import Objects.muon
from Objects.muon import Muon
import random as rnd
from Objects.scintillator import Scintillator
from ursina import Vec3

objects = []
from Model.settings import SCINTILLATOR_SIZE_X, SCINTILLATOR_SIZE_Y, SCINTILLATOR_SIZE_Z, VEC0_3D


def invoke_draw_line(start, end, thickness, color):
    return viewer.draw_line(start, end, thickness, color)


def add_to_objects_list(object):
    objects.append(object)
    return object


def create_n_random_muons(n):
    """
    This function will create and print n muons of varying energies and angels
    :param n: Number of muons
    :return: Array of all muons
    """
    scintillator_ref = [x for x in objects if isinstance(Scintillator, x)]
    scintillator_ref = scintillator_ref[0]
    if len(scintillator_ref) < 0:
        print("Please define a scintillator fist!")
        return
    for i in range(1, n + 1):
        end = rnd.randint(scintillator_ref.pos - scintillator_ref.size / 2,
                          scintillator_ref.pos + scintillator_ref.size / 2)
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

    scint = Scintillator()

    objects.insert(-1, Scintillator(scint_pos,
                                    scint_size / 2, ))  # TODO: understand if scintillator's size is from middle point or some edge point
    return scint
