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
        self.start_beam = lerp(self.start, self.end, .95)

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

    def calculate_collisions(self):  # TODO: print only hit ground, debug, probably causes 10x end point
        hits_on_scint_0 = []
        hits_on_scint_1 = []
        hits_on_scint_2 = []
        hits_on_scint_3 = []
        hits_on_scint_4 = []

        self.hit_info = raycast(self.start_beam, self.end - self.start_beam,
                                distance=size_of_vec(self.start_beam - self.end), debug=False)

        entities = self.hit_info.entities

        scint_entities = [entity for entity in entities if isinstance(entity, Scintillator)]

        x = len(scint_entities)

        if len(set(scint_entities)) < len(scint_entities):
            # print("Muon " + str(self) + " Registered a hit the same scintillator twice, will be disposed.")
            self.kill_muon()
            return -1, -1, -1, -1, -1, None
        elif x == NUMBER_OF_SCINTS:
            direction = (self.end - self.start) / size_of_vec(self.end - self.start)
            # print("Muon " + str(self) + " Did pass through 5 scintillators, will be kept!.")
            # print(direction*SCINTILLATOR_SPACING)
            hit_points = [0 for i in range(x)]
            for i in range(0, x):
                hit_points[i] = direction * i * SCINTILLATOR_SPACING + self.hit_info.point

            # if hit_points[0] == self.hit_info.point:
            #   print("First hit point in sync")
            self.color = color.cyan

        else:
            # print("Muon " + str(self) + " Did not pass through 5 scintillators, will be disposed.")
            self.kill_muon()
            return -1, -1, -1, -1, -1, None
        for entity in entities:
            if isinstance(entity, Scintillator):
                if entity.level == 0:
                    hits_on_scint_0.append(hit_points[0].xy)
                if entity.level == 1:
                    hits_on_scint_1.append(hit_points[1].xy)
                if entity.level == 2:
                    hits_on_scint_2.append(hit_points[2].xy)
                if entity.level == 3:
                    hits_on_scint_3.append(hit_points[3].xy)
                if entity.level == 4:
                    hits_on_scint_4.append(hit_points[4].xy)

        return hits_on_scint_0, hits_on_scint_1, hits_on_scint_2, hits_on_scint_3, hits_on_scint_4, self

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
