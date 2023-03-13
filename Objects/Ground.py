class Ground:
    """
    This class represents ground object
    """
    def __init__(self, pos, size, rotation, mesh_sol, mesh_wire):
        self.size = size
        self.pos = pos
        self.rotation = rotation
        self.mesh_sol = mesh_sol
        self.mesh_wire = mesh_wire


