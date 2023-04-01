from ursina import Vec3, Entity


class Scintillator(Entity):
    def __init__(self, level, pos, size, rotation, mesh_sol, mesh_wire):
        self.pos = pos
        self.size = size
        self.rotation = rotation
        self.mesh_sol_ref = mesh_sol
        self.mesh_wire_ref = mesh_wire
        Entity.__init__(self)

    def scintillate(self, muon):
        pass


