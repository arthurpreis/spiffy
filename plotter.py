from mayavi.mlab import *
from mayavi import mlab
import numpy as np

class Plotter:
    def __init__(self):
        pass

    @staticmethod
    def plot_trajectory(trajectory,**kwargs):
        plot = plot3d(trajectory[0, :], trajectory[1, :], trajectory[2, :],
                      **kwargs)
        return plot

    @staticmethod
    def plot_separation(pos1, pos2, **kwargs):
        plot = plot3d([np.double(pos1[0]), np.double(pos2[0])],
                      [np.double(pos1[1]), np.double(pos2[1])],
                      [np.double(pos1[2]), np.double(pos2[2])],
                      **kwargs)
        return plot

    #@staticmethod
    #def plot_separation(self, trajectory, time):
    #    pass

    @staticmethod
    def plot_vector(self, pos, dir):
        pass

    @staticmethod
    def plot_point(pos, **kwargs):
        #a = np.double(pos[0])
        plot = points3d(np.double(pos[0]),
                        np.double(pos[1]),
                        np.double(pos[2]),
                        **kwargs)#scale_factor = .01, color = (1, 0, 0))
        return plot
