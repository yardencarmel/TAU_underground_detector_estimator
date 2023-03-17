from ursina import *
from Objects.line import Line
from Objects.Muon import Muon
from View.viewer import draw_cube, setup_window, change_app_title
from Model.settings import *
import Objects.controller as cntrl


def main(argv):
    # TODO: check why title won't change
    app = Ursina(title='TAU Muon Estimator')
    setup_window(app, False, False, True, True)
    change_app_title(app, "TAU Muon Estimator")

    # # Define the 3D line
    # path = (Vec3(0, 0, 0), Vec3(0, 1, 0))
    #
    # thicknesses = (0.1, 0.1)
    x = Line(Vec3(100, 0, 0), Vec3(-100, 0, 0), 0.5, color.red)
    y = Line(Vec3(0, 100, 0), Vec3(0, -100, 0), 0.5, color.green)
    z = Line(Vec3(0, 0, 100), Vec3(0, 0, -100), 0.5, color.blue)
    # testmuon = Muon(VEC0_3D, Vec3(0, -3, 0), 1 * GeV, line)
    # testmuon.kill_muon()
    # testcube = draw_cube(Vec3(0, 0, 0), Vec3(4, 1, 0.0254), color.pink)
    scint = cntrl.create_scintillator()
    muons = cntrl.create_n_random_muons(10000)
    hit_points = [muon.end for muon in muons]
    start_points = [muon.start for muon in muons]
    cntrl.create_start_hist(start_points,100)
    cntrl.create_hits_hist(scint, hit_points,100)
    # cntrl.create_ground(10, Vec3(1, 1, 0), Vec3(1, 2, 2))

    EditorCamera()  # TODO: build a better camera
    # origin = Entity(model='cube', color=color.brown)
    # origin.scale *= .25

    # Run the game loop
    app.run()


if __name__ == "__main__":
    main(sys.argv)
