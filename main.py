from ursina import *
from Objects.line import Line
from Objects.Muon import Muon
from View.viewer import setup_window, change_app_title
from Model.settings import *
import Objects.controller as cntrl


#import multiprocessing as mp
import concurrent.futures

class Test():
    def __int__(self, pos):
        self.pos = pos

    @staticmethod
    def create_test(n):
        tests = []
        for i in range(n):
            tests.append(Test())
        return tests
def main(argv):
    tests = Test.create_test(5)
    # TODO: check why title won't change
    app = Ursina(title='TAU Muon Estimator')
    setup_window(app, False, False, True, True)
    change_app_title(app, "TAU Muon Estimator")

    # Create XYZ axes
    x = Line(Vec3(100, 0, 0), Vec3(0, 0, 0), 0.5, color.red)
    y = Line(Vec3(0, 100, 0), Vec3(0, 0, 0), 0.5, color.green)
    z = Line(Vec3(0, 0, 100), Vec3(0, 0, 0), 0.5, color.blue)

    # Returns a list of scintillators objs that derives from Ursina's Entity
    scintillators = cntrl.create_scintillator(NUMBER_OF_SCINTS)

    # Creates the ground map (cubic ground made of smaller 1m^3 cubes), with vacancy position and size
    #cntrl.create_ground(MAP_SIZE, Vec3(1, 1, 0), Vec3(1, 2, 2))

    processes = []
    #queue = multiprocessing.Queue()
    #muons = []


    # Run the creation of NUMBER_OF_MUONS in parallel.
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     f1 = executor.submit(cntrl.create_n_random_muons, (NUMBER_OF_MUONS, scintillators,))
    #     print(f1.result())

    ##### DISREGARD#####
    # for _ in range(5):
    #     p = mp.Process(target=cntrl.create_n_random_muons, args=(NUMBER_OF_MUONS, shared_scintillator[0], muons,))
    #     processes.append(p)
    #     p.start()
    # for process in processes:
    #     process.join()
        #muons = muons + process.exitcode
    muons = cntrl.create_n_random_muons(NUMBER_OF_MUONS, scintillators)
    # print(muons[0].pos)

    ##### END DISREGARD#####

    # Check for each muon collision. TODO: make parallel.
    cntrl.check_muons_collisions(muons)

    # Create histograms using the randomized start points.
    # Right now we only consider muons that hit 5 scintillators, as the collision detection is quirky.
    # start_points = [muon.start for muon in muons]



    # cntrl.create_hits_hist(end_points, 50)

    # Create a camera
    EditorCamera()

    # Run app
    app.run()


    # cntrl.create_ground(Vec3(19, 19, 7), Vec3(2, 2, 1), Vec3(5, 5, 5))

if __name__ == "__main__":
    main(sys.argv)
