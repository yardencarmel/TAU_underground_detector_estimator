from ursina import destroy, raycast

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
        self.hit_info = raycast(self.start, calculate_direction_between_points(self.start, self.end), ignore=(self,),
                                distance=size_of_vec(self.start - self.end), debug=False)

    def kill_muon(self):
        """
        This function will destroy the muon that owns it.
        :return: None
        """
        destroy(self.mesh_ref)
        del self
        return None

    def calculate_muon_collisions(self):  # TODO: print only hit ground
        entities = self.hit_info.entities
        for entity in entities:
            if isinstance(entity, Objects.Ground.Ground):
                print(str(entity) + " is hit at point: " + self.hit_info.point)
