from ursina import Entity, Mesh
import controller


class Line:
    def __init__(self, start, end, thickness, color):
        self.start = start
        self.end = end
        self.thickness = thickness
        self.color = color
        self.line_entity = controller.invoke_draw_line(self.start, self.end, self.thickness, self.color)


