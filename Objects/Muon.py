from ursina import destroy, raycast, color, Vec3, Entity, Mesh, inverselerp, lerp
import Objects.controller as cntrl
from Objects.scintillator import Scintillator
from Model.settings import *
import Objects.Ground
from Model.VectorCalculations import calculate_direction_between_points, size_of_vec
# from numba import jit, cuda

class Muon(Entity):
    """
    Object class for muons
    """

    def __init__(self, index, start, end, energy, mesh):
        """
        Initialization function for a muon
        :param start: Starting point
        :param end: End point
        :param energy: Energy, used for calculating scintillation.
        :param mesh: Mesh reference.
        """
        self.start = start
        self.end = end
        # self.momentum = momentum
        self.energy = energy
        self.mesh_ref = mesh
        self.index = index
        self.hit_info = None
        self.start_beam = lerp(self.start, self.end, .6)
        Entity.__init__(self, model=Mesh(vertices=[start, end], mode='line', thickness=0.1), color=MUON_COLOR)

    def kill_muon(self):
        """
        This function will destroy the muon that owns it.
        :return: None
        """
        destroy(self.mesh_ref)
        self.model = None
        del self
        return None


    def calculate_collisions(self):  # TODO: print only hit ground
        hits_on_scint_0 = []
        hits_on_scint_1 = []
        hits_on_scint_2 = []
        hits_on_scint_3 = []
        hits_on_scint_4 = []
        self.hit_info = raycast(self.start_beam, self.end - self.start_beam,
                                distance=size_of_vec(self.start_beam - self.end), debug=False)
        # print("RAYCAST LEN: "+str(self.hit_info.distance))
        entities = self.hit_info.entities
        x = len(entities)
        if x < 4:
            print("Muon " + str(self) + " Did not pass through 4 scintillators, will be disposed.")
            self.kill_muon()
            return
        if len(set(entities)) < len(entities):
            print("Muon " + str(self) + " Registered a hit the same scintillator twice, will be disposed.")
            self.kill_muon()
            return
        if x == 4:
            self.color = color.cyan
            cntrl.passed_muons.append(self)
        for entity in entities:
            if isinstance(entity, Scintillator):
                if entity.level == 0:
                    hits_on_scint_0.append(self.hit_info.point.xy)
                if entity.level == 1:
                    hits_on_scint_1.append(self.hit_info.point.xy)
                if entity.level == 2:
                    hits_on_scint_2.append(self.hit_info.point.xy)
                if entity.level == 3:
                    hits_on_scint_3.append(self.hit_info.point.xy)
                if entity.level == 4:
                    hits_on_scint_4.append(self.hit_info.point.xy)
        return hits_on_scint_0, hits_on_scint_1, hits_on_scint_2, hits_on_scint_3, hits_on_scint_4
    def print_collision(self, entity, position):
        print("*************************")
        print("Muon " + str(self.index) + " hit " + str(entity) + " at " + str(position))
        print("*************************")

    def on_click(self):
        print("self")

    def print_start(self):
        print(str(self.start))
    def print_end(self):
        print(str(self.end))