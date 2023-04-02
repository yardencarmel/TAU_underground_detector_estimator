from ursina import *
from Objects.line import Line
from Objects.Muon import Muon
from View.viewer import setup_window, change_app_title
from Model.settings import *
import Objects.controller as cntrl


def main(argv):
    # TODO: check why title won't change
    app = Ursina(title='TAU Muon Estimator')
    setup_window(app, False, False, True, True)
    change_app_title(app, "TAU Muon Estimator")

    # Create XYZ axes
    x = Line(Vec3(100, 0, 0), Vec3(-100, 0, 0), 0.5, color.red)
    y = Line(Vec3(0, 100, 0), Vec3(0, -100, 0), 0.5, color.green)
    z = Line(Vec3(0, 0, 100), Vec3(0, 0, -100), 0.5, color.blue)

    scints = cntrl.create_scintillator(NUMBER_OF_SCINTS) # NUMBER_OF_SCINTS = 4


    muons = cntrl.create_n_random_muons(15)
    for muon in muons:
        muon.print_start()
    print("*************************************")
    for muon in muons:
        muon.print_end()
    print("*************************************")
    cntrl.check_muons_collisions(muons)
    #cntrl.create_ground(10, Vec3(1, 1, 0), Vec3(1, 2, 2))

    EditorCamera()  # TODO: build a better camera
    app.run()


    # muons = cntrl.create_n_random_muons(10)
    # hit_points = [muon.end for muon in muons]
    # start_points = [muon.start for muon in muons]
    # cntrl.create_start_hist(start_points, 50)
    # cntrl.create_hits_hist(hit_points, 50)
    # cntrl.create_ground(Vec3(19, 19, 7), Vec3(2, 2, 1), Vec3(5, 5, 5))

if __name__ == "__main__":
    main(sys.argv)
