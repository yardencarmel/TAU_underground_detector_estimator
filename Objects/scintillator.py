from ursina import Vec3, Entity, color


class Scintillator(Entity):
    def __init__(self, level, pos, size, rotation, mesh_wire):
        self.pos = pos
        self.size = size
        self.rotation = rotation
        self.mesh_wire = mesh_wire
        Entity.__init__(self, scale = size, position = pos, model = 'cube', collider = 'box', color = color.pink)

    def scintillate(self, muon):
        pass

    def on_click(self):
        print("self")

