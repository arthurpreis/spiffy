from spiffy.orbit import *

if __name__ == '__main__':
    # testing the orbit and plotter classes
    mlab.figure(size = (800, 600))

    N = ReferenceFrame('N')
    t = linspace(0, 6.3, 2000)  # numpy array
    #ti = 0.4
    # creates 3 orbits. Two objects orbiting a main body
    #earth_orbit = CircularOrbit3D(N, None, 1, 1, 0, color = (0.2, 0.7, 0.3))
    sat1_orbit = CircularOrbit3D(N, radius = 1, omega = 1, inclination = 5*(np.pi/180), ascNode = 0*(np.pi/180), phase = (0+180)*(np.pi/180), color = (1, 0, 0))
    sat2_orbit = CircularOrbit3D(N, radius = 1, omega = 1, inclination = 5*(np.pi/180), ascNode = 120*(np.pi/180), phase = (-120+60)*(np.pi/180), color = (0, 1, 0))
    sat3_orbit = CircularOrbit3D(N, radius = 1, omega = 1, inclination = 5*(np.pi/180), ascNode = 240*(np.pi/180), phase = (-240-60)*(np.pi/180), color = (0, 0, 1))

    orbits = [sat1_orbit, sat2_orbit, sat3_orbit]
    #for i, ti in enumerate(t):
    #i = 1
    #ti = 0.4
    for i in range(100):
        ti = t[i*20]
        for obt in orbits:
            Plotter.plot_trajectory(obt.get_trajectory(t, frame = N),
                                    tube_radius = None, color = obt.color,
                                    opacity = 0.2)
            Plotter.plot_point(obt.get_position_matrix(ti, N),
                               scale_factor = 0.02, color = obt.color)

        sat1_pos = sat1_orbit.get_position_matrix(ti, N)
        sat2_pos = sat2_orbit.get_position_matrix(ti, N)
        sat3_pos = sat3_orbit.get_position_matrix(ti, N)
        avg_pos = (sat1_pos + sat2_pos + sat3_pos)/3

        Plotter.plot_separation(sat1_pos, sat2_pos,
                                color = (0.8, 0.8, 0.8), tube_radius = None,)
        Plotter.plot_separation(sat1_pos, sat3_pos,
                                color = (0.8, 0.8, 0.8), tube_radius = None,)
        Plotter.plot_separation(sat2_pos, sat3_pos,
                                color = (0.8, 0.8, 0.8), tube_radius = None,)
        Plotter.plot_point([0, 0, 0], scale_factor = .5, color = (0.1,.8,0.6))
        Plotter.plot_point(avg_pos, scale_factor = 0.01, color = (0.8,0.8,0.8))
        plane_vec1 = sat1_orbit.get_direction_matrix(sat2_orbit, ti, N)
        plane_vec2 = sat1_orbit.get_direction_matrix(sat3_orbit, ti, N)
        #print("main:")
        #print(sat1_orbit.get_position_matrix(0.1, N))
        #print(sat2_orbit.get_position_matrix(0.1, N))
        cr = plane_vec1.cross(plane_vec2)
        #print(plane_vec)
        Plotter.plot_vector(avg_pos, cr,  color = (0.8,0.8,0.8),
                            scale_factor = 4)
        filename = "test_cartwheel" + str(i) + ".png"

        mlab.view(distance = 4, elevation = 80)
        mlab.show()  # calls mayavi show
        #mlab.savefig(filename)
        mlab.clf()