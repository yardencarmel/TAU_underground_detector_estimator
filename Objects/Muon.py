from ursina import destroy, raycast
import Objects.controller as cntrl

import Objects.Ground
from Model.VectorCalculations import calculate_direction_between_points, size_of_vec


class Muon:
    """
    Object class for muons
    """

    def __init__(self, start, end, energy, mesh):
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

        self.hit_info = None

    def kill_muon(self):
        """
        This function will destroy the muon that owns it.
        :return: None
        """
        destroy(self.mesh_ref)
        del self
        return None

    def calculate_collisions(self):  # TODO: print only hit ground
        self.hit_info = raycast(self.start, self.end - self.start,
                                distance=size_of_vec(self.start - self.end), ignore=tuple(cntrl.wireframes), debug=False)
        entities = self.hit_info.entities
        for entity in entities:
            print(type(entity))
            if entity in cntrl.ground_tiles:
                print(str(entity) + " is hit at point: " + self.hit_info.point)
        return entities


