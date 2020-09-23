from sympy.physics.mechanics import *
from matplotlib.pyplot import plot, show
import numpy as np


class Orbit:
    def __init__(self, parentFrame, focus, eccentricity, semimajorAxis, inclination,
                 ascendingNodeLongitude, periapsisArgument):
        self.focus = focus
        self.parentFrame = parentFrame
        self.eccentricity = eccentricity
        self.semimajorAxis = semimajorAxis
        self.inclination = inclination
        self.ascendingNodeLongitude = ascendingNodeLongitude
        self.periapsisArgument = periapsisArgument

        self.frame = parentFrame.orientnew('frame', 'Body',
                                           (self.inclination,
                                            self.ascendingNodeLongitude,
                                            self.periapsisArgument),
                                           '123')

        self.trueAnomaly = 0

    def initial_position(self):
        pass

    def get_position(self, epoch, frame=None):
        # given an epoch, returns a vector for position
        # todo pass other frame argument
        if frame is None:
            frame = self.frame

        r = self.semimajorAxis * (1 - np.power(self.eccentricity, 2.0)) / \
            (1 + self.eccentricity * np.cos(epoch))
        x = frame.x * r * np.cos(epoch)
        y = frame.y * r * np.sin(epoch)
        z = frame.z
        return x + y + z

    def plot_orbit(self, frame=None):
        # plots orbit using matplotlib
        # todo pass other frame
        if frame is None:
            frame = self.frame

        # todo calculate period before choosing t
        t = np.linspace(0, 1000, 10000)
        pos_x = []
        pos_y = []
        pos_z = []

        for idx, ti in enumerate(t):
            vec = self.get_position(ti).to_matrix(frame)
            pos_x.append(vec[0])
            pos_y.append(vec[1])
            pos_z.append(vec[2])

        plot(pos_x[:], pos_y[:])
        show()


if __name__ == '__main__':
    solar = ReferenceFrame('solar')
    orbit1 = Orbit(solar, 0, 1, 0.1, 0, 0)
    orbit1.plot_orbit()
