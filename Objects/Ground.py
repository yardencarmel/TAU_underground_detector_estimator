from ursina import destroy, Entity, Cube


class Ground(Entity):
    """
    This class represents ground object
    """

    def __init__(self, pos, size, rotation, mesh_sol, mesh_wire, collider):
        Entity.__init__(self, position=pos, rotation=rotation, scale=size, collider=collider, model=mesh_sol)
        self.size = size
        self.pos = pos
        self.rotation = rotation
        self.mesh_sol = mesh_sol
        self.mesh_wire = mesh_wire
        self.collider = collider

    def destroy_ground(self):
        destroy(self.mesh_sol)
        destroy(self.mesh_wire)
        del self
        return None
