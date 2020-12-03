from spiffy.plotter import Plotter
import numpy as np
import open3d
import numpy
from mayavi.mlab import *


def test_mesh():
    """A very pretty picture of spherical harmonics translated from
    the octaviz example."""
    pi = np.pi
    cos = np.cos
    sin = np.sin
    dphi, dtheta = 1 * pi / 180, 1 * pi / 180
    [phi, theta] = np.mgrid[0:2 * pi+dphi:dphi,
                   0: pi + dtheta:dtheta]

#    print(phi.shape)
#    print(theta.shape)
    X = []
    Y = []
    Z = []
    r = 1
    x = r * sin(phi) * cos(theta)
    #print(x[][0])
    y = r * cos(phi)
    z = r * sin(phi) * sin(theta)
    print(x.shape)
    with open("./CoordenadasFX.txt", 'r') as file:
        for i, line in enumerate(file):
            #if i % 10 == 0:
            s = line.split()
            X.append(float(s[0]))
            Y.append(float(s[1]))
            Z.append(float(s[2]))
            print(i)
            x[int(np.floor(i/181))][i % 181] = float(s[0])
            y[int(np.floor(i/181))][i % 181] = float(s[1])
            z[int(np.floor(i/181))][i % 181] = float(s[2])


    return contour3d(x, y, z, np.ones(x))

test_mesh()