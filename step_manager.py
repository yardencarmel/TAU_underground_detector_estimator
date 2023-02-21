from Objects.muon import Muon
from Objects.scintillator import Scintillator


class StepManager:
    def __init__(self):
        self.scintillator = Scintillator()
        pass

    def muon_fate(self, muon, distances):
        energy_left = muon.energy
        for distance in distances:
            energy_left -= distance * 0.6
        if energy_left < 0:
            Muon.kill_muon(muon)
        else:
            self.scintillator.scintillate(muon)

#  TODO: find a meaning for this, or delete.
