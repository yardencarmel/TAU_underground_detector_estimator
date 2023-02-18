from ursina import *

app = Ursina()


e = Entity(model='cube', color=color.orange, position=(0,0,1), scale=1.5, rotation=(0,0,45), texture='brick')

EditorCamera()

app.run()
