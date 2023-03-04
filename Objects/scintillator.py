from ursina import Vec3


class Scintillator:
    def __init__(self, pos, size, rotation, mesh_sol, mesh_wire):
        self.pos = pos
        self.size = size
        self.rotation = rotation
        self.mesh_sol_ref = mesh_sol
        self.mesh_wire_ref = mesh_wire

    def scintillate(self, muon):
        pass


