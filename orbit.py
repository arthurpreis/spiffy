import numpy as np
from mayavi.mlab import *
from mayavi import mlab
from sympy.physics.mechanics import *
from numpy import cos, sin, linspace
from plotter import Plotter


class Orbit:
    def __init__(self, frame, center, color = (0, 0, 0)):
        self.frame = frame
        self.center = center
        self.color = color

    def get_position(self, epoch) -> Vector:
        pass

    def get_trajectory(self, epoch: np.array, center = None, frame = None):
        if type(self) == CircularOrbit3D:
            pos = np.zeros_like([epoch, epoch, epoch], dtype = float)
        elif type(self) == CircularOrbit2D:
            pos = np.zeros_like([epoch, epoch], dtype = float)

        if frame is None:
            frame = self.frame

        for idx, ti in enumerate(t):
            if center is None:
                vec = self.get_position(ti).to_matrix(frame)
            else:
                vec = (self.get_position(ti) - center.get_position(ti)).to_matrix(frame)
            pos[:, idx] = vec[:]
        return pos


class CircularOrbit2D(Orbit):
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
    def __init__(self, parentFrame, frame = None, center = None, radius: float = 0,
                 omega: float = 0, inclination: float = 0, phase: float = 0,
                 ascNode: float = 0, color = (0, 0, 0)):
        super().__init__(frame, center, color)
        self.frame = parentFrame.orientnew('frame', 'Axis', (inclination, frame.x))
        self.radius = radius
        self.omega = omega
        self.phase = phase
        self.ascNode = ascNode

    def get_position(self, epoch, frame = None):
        # given an epoch, returns a vector for position
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
    N = ReferenceFrame('N')
    # frame, center, radius, omega, inclination,
    # phase = 0.0, ascNode = 0.0
    orbit = CircularOrbit3D(N, N, None, 1, 1, 0, color = (1, 1, 1))
    t = linspace(0, 0.5, 500)
    v = orbit.get_trajectory(t, frame = N)
    sat1_orbit = CircularOrbit3D(N, N, center = orbit, radius = 0.1,
                                 omega = 100, inclination = np.pi / 2,
                                 color = (0, 1, 0))
    sat2_orbit = CircularOrbit3D(N, N, center = orbit, radius = 0.08,
                                 omega = 120, inclination = np.pi / 6,
                                 color = (0, 0, 1))

    Plotter.plot_trajectory(v, tube_radius = None, color = orbit.color)

    Plotter.plot_trajectory(sat1_orbit.get_trajectory(t, frame = N),
                            tube_radius = None, color = sat1_orbit.color)
    Plotter.plot_trajectory(sat2_orbit.get_trajectory(t, frame = N),
                            tube_radius = None, color = sat2_orbit.color)

    Plotter.plot_point(sat1_orbit.get_position(0, N).to_matrix(N),
                       scale_factor = 0.01, color = sat1_orbit.color)
    Plotter.plot_point(sat2_orbit.get_position(0, N).to_matrix(N),
                       scale_factor = 0.01, color = sat2_orbit.color)

    Plotter.plot_separation(sat1_orbit.get_position(0, N).to_matrix(N),
                            sat2_orbit.get_position(0, N).to_matrix(N),
                            tube_radius = None, color = (1, 1, 1))
    mlab.show()
