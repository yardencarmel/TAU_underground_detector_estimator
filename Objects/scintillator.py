from ursina import Vec3, Entity, color
from Model.settings import SCINTILLATOR_COLOR

class Scintillator(Entity):
    def __init__(self, level, pos, size, rotation, mesh_wire):
        self.level = level
        self.pos = pos
        self.size = size
        self.rotation = rotation
        self.mesh_wire = mesh_wire
        Entity.__init__(self, position=pos, scale=size, model='cube', collider='box', color=SCINTILLATOR_COLOR,
                        rotation=rotation)

    def scintillate(self, muon):
        pass

    def on_click(self):
        print("self")
