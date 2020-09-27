import numpy as np
from mayavi import mlab
from sympy.physics.mechanics import *
from numpy import cos, sin, linspace
from plotter import Plotter


class Orbit:
    '''Base orbit class that is used to build circular and eliptical orbits
    frame: sympy.ReferenceFrame object
    center: point/trajectory of the attractor #todo rename?
    color: (R,G,B) tuple to be used when plotting trajectory and body'''

    def __init__(self, frame, center, color = (0, 0, 0)):
        self.frame = frame
        self.center = center
        self.color = color

    def get_position(self, epoch) -> Vector:
        pass

    def get_trajectory(self, epoch: np.array, center = None, frame = None):
        '''Returns a 2D or 3D numpy array of results from get_position()
        over time'''
        if type(self) == CircularOrbit3D:
            pos = np.zeros_like([epoch, epoch, epoch], dtype = float)
        elif type(self) == CircularOrbit2D:
            pos = np.zeros_like([epoch, epoch], dtype = float)

        if frame is None:
            # todo: better explanation of how sympy frames work here,
            # some way to add the possib. of plotting around earth
            frame = self.frame

        for idx, ti in enumerate(t):
            # calls get_position() for each time, subtract center position
            if center is None:
                vec = self.get_position(ti).to_matrix(frame)
            else:
                vec = (self.get_position(ti) -
                       center.get_position(ti)).to_matrix(frame)
            pos[:, idx] = vec[:]
        return pos


class CircularOrbit2D(Orbit):
    '''2D circular orbit, built as toy model of 3D orbit. DEPRECATED'''

    def __int__(self, frame, center, radius = 0.0,
                omega = 0.0, phase = 0.0):
        super().__init__(frame, center)
        self.radius = phase
        self.omega = phase
        self.phase = phase

    def get_position(self, epoch, frame = None):
        # given an epoch, returns a vector for position
        if frame is None:
            frame = self.frame

        r = self.radius
        om = self.omega
        ph = self.phase
        center = self.center
        x = r * cos(om * epoch + ph) * frame.x
        y = r * sin(om * epoch + ph) * frame.y

        if center is None:
            return x + y
        elif type(center) is CircularOrbit2D:
            return x + y + center.get_position(epoch)

    def plot_orbit(self, center = None):
        # plots orbit using matplotlib
        # todo pass other frame
        # todo calculate period before choosing t
        t = linspace(0, 6.28, 10000)
        pos_x = np.zeros_like(t, dtype = float)
        pos_y = np.zeros_like(t, dtype = float)

        for idx, ti in enumerate(t):
            if center is None:
                vec = self.get_position(ti).to_matrix(self.frame)
            else:
                vec = (self.get_position(ti) - center.get_position(ti)).to_matrix(self.frame)
            pos_x[idx] = vec[0]
            pos_y[idx] = vec[1]

        return pos_x[:], pos_y[:]


class CircularOrbit3D(Orbit):
    '''Model of a ideal 3D orbit'''

    def __init__(self, parentFrame, frame = None, center = None,
                 radius: float = 0, omega: float = 0, inclination: float = 0,
                 phase: float = 0, ascNode: float = 0, color = (0, 0, 0)):
        super().__init__(frame, center, color)
        self.frame = parentFrame.orientnew('frame', 'Axis', (inclination, frame.x))
        # todo: orient new frame with 'Space'
        self.radius = radius
        self.omega = omega  # todo: rename parm
        self.phase = phase  # todo: rename parm
        self.ascNode = ascNode  # todo: rename parm

    def get_position(self, epoch, frame = None):
        '''given an epoch, returns a sympy vector for position'''
        # todo pass other frame argument
        r = self.radius
        om = self.omega
        ph = self.phase
        if frame is None:
            frame = self.frame

        x = r * cos(om * epoch + ph) * frame.x
        y = r * sin(om * epoch + ph) * frame.y
        z = 0 * frame.z
        if self.center is None:
            return x + y + z
        elif type(self.center) is CircularOrbit3D:
            return x + y + z + self.center.get_position(epoch).express(frame)

    def plot_orbit2D(self, center = None):
        # DEPRECATED
        t = linspace(0, 5, 3000)
        pos_x = []
        pos_y = []

        for idx, ti in enumerate(t):
            if center is None:
                vec = self.get_position(ti).to_matrix(self.frame)
            else:
                vec = (self.get_position(ti)).to_matrix(self.frame)
            pos_x.append(vec[0])
            pos_y.append(vec[1])

        return pos_x[:], pos_y[:]


if __name__ == '__main__':
    # testing the orbit and plotter classes
    N = ReferenceFrame('N')
    t = linspace(0, 0.5, 500)  # numpy array

    # creates 3 orbits. Two objects orbiting a main body
    earth_orbit = CircularOrbit3D(N, N, None, 1, 1, 0, color = (1, 1, 1))
    sat1_orbit = CircularOrbit3D(N, N, center = earth_orbit, radius = 0.1,
                                 omega = 100, inclination = np.pi / 2,
                                 color = (0, 1, 0))
    sat2_orbit = CircularOrbit3D(N, N, center = earth_orbit, radius = 0.08,
                                 omega = 120, inclination = np.pi / 6,
                                 color = (0, 0, 1))

    # testing plotter functionalities
    orbits = [earth_orbit, sat1_orbit, sat2_orbit]
    for obt in orbits:
        Plotter.plot_trajectory(obt.get_trajectory(t, frame = N),
                                tube_radius = None, color = obt.color)
        Plotter.plot_point(obt.get_position(0, N).to_matrix(N),
                           scale_factor = 0.01, color = obt.color)

    Plotter.plot_separation(sat1_orbit.get_position(0, N).to_matrix(N),
                            sat2_orbit.get_position(0, N).to_matrix(N),
                            tube_radius = None, color = (1, 1, 1))
    Plotter.plot_vector(sat1_orbit.get_position(0, N).to_matrix(N),
                        sat2_orbit.get_position(0, N).to_matrix(N) -
                        sat1_orbit.get_position(0, N).to_matrix(N))

    mlab.show()  # calls mayavi show
