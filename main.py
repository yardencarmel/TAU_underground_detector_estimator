from ursina import *
from Objects.line import Line

def main(argv):

    app = Ursina()

    # Define the 3D line
    path = (Vec3(0, 0, 0), Vec3(0, 1, 0))
    thicknesses = (0.1, 0.1)
    line = Line(Vec3(0,1,0),Vec3(0.1,-1,0),10,color.green)
    EditorCamera()
    origin = Entity(model='cube', color=color.brown)
    origin.scale *= .25

    # Run the game loop
    app.run()


if __name__ == "__main__":
    main(sys.argv)
