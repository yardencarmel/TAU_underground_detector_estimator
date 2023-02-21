from ursina import Vec3


class Scintillator:
    def __init__(self, pos, size, rotation):
        self.pos = pos
        self.size = size
        self.rotation = rotation
        pass

    def scintillate(self, muon):
        pass

    @property
    def pos(self, start_pos=vec(0, 0, 0)):
        self.pos = start_pos
