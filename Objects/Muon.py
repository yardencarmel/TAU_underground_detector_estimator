from ursina import destroy, raycast, color, Vec3, Entity, Mesh, lerp
import Objects.controller as cntrl
from Objects.scintillator import Scintillator
from Model.settings import *
import Objects.Ground
from Model.VectorCalculations import calculate_direction_between_points, size_of_vec


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
        self.start = lerp(start, Vec3(0), .1)
        self.end = end
        # self.momentum = momentum
        self.energy = energy
        self.mesh_ref = mesh
        self.index = index
        self.hit_info = None
        Entity.__init__(self, model=Mesh(vertices=[start, end], mode='line', thickness=0.1), color=MUON_COLOR)

    def kill_muon(self):
        """
        This function will destroy the muon that owns it.
        :return: None
        """
        destroy(self.mesh_ref)
        del self
        return None

    def calculate_collisions(self):  # TODO: print only hit ground
        self.hit_info = raycast(self.start/10, self.end - self.start,
                                distance=size_of_vec(self.start - self.end), debug=True)
        entities = self.hit_info.entities
        x = len(entities)
        if x == 0:
            self.color = color.cyan
        if x == 1:
            self.color = color.brown
        if x == 2:
            self.color = color.red
        if x == 3:
            self.color = color.orange
        if x == 4:
            self.color = color.gold
        if x == 5:
            self.color = color.black
        for entity in entities:
            print(type(entity))
            print(entity.name)
            if isinstance(entity, Scintillator):
                self.print_collision(entity, self.hit_info.point)
        return entities

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