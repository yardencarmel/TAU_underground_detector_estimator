import View.viewer as viewer
import Objects.line
import Objects.muon
from muon import Muon
import random as rnd
from scintillator import Scintillator
from ursina import Vec3
objects = []


def invoke_draw_line(start, end, thickness, color):
    return viewer.create_line(start, end, thickness, color)


def add_to_objects_list(object):
    objects.append(object)
    return object

def create_n_random_muons(n):
    scintillator_ref = [x for x in objects if isinstance(Scintillator(), x)]
    if len(scintillator_ref) < 0:
        print("Please define a scintillator fist!")
        return
    for i in range(1,n+1):
        end = rand
        muon_i = Muon() #  TODO: randomize locations and momentas.

def create_scintillator():
    scintillator_ref = [x for x in objects if isinstance(Scintillator(), x)]
    if len(scintillator_ref) > 0:
        print("A scintillator is already defined!")
        return
    scint_size = Vec3(1,1,1) #  in meters
    scint_pos = Vec3(0,0,0) #  in meters
    scint_rot = Vec3(0,0,0) #  in degrees
    else:
        objects.insert(-1, Scintillator(scint_pos,scint_size/2,)) #  TODO: understand if scintillator's size is from middle point or some edge point
