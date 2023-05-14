from ursina import destroy, Entity, Cube
from Model.settings import GROUND_COLOR

class Ground(Entity):
    """
    This class represents ground object
    """

    def __init__(self, pos, size, rotation, mesh_wire):
        self.size = size
        self.pos = pos
        self.rotation = rotation
        self.mesh_wire = mesh_wire
        Entity.__init__(self, position=pos, origin=pos, scale=size, model='cube', collider='box', color=GROUND_COLOR,
                        rotation=rotation)


    def destroy_ground(self):
        destroy(self.mesh_sol)
        destroy(self.mesh_wire)
        del self
        return None
