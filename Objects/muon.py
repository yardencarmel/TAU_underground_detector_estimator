from ursina import color, destroy
import line


class Muon:
    def __init__(self, start, end, momentum, energy):
        self.start = start
        self.end = end
        self.momentum = momentum
        self.energy = energy
        self.mesh = line(self.start, self.end, 0.1 * energy, color.green)

    def kill_muon(self):
        destroy(self.mesh) #  TODO: check this works
        del self
        return None
