# SPIFFY
# Space Interferometer Python Framework
# Arthur Reis 2020
from sympy.physics.mechanics import ReferenceFrame, Point
from orbit import Orbit
import numpy as np
# from matplotlib.pyplot import plot, show

# Create solar system frame of reference

# Solar = ReferenceFrame('Solar')

# Create solar system
solar = ReferenceFrame('Solar')
Sun = Point('Sun')
Sun.set_vel(solar, 0)

earth_orbit = Orbit(solar, Sun, 0, 1, 0.1, 0, 0)
earth_pos = earth_orbit.get_position(0)
Earth = Point('Earth')
Earth.set_pos(Sun, earth_pos)

earth_frame = solar.orientnew('Earth', 'Body', (0.2, 0, 0), 123)
sat_orbit = Orbit(earth_frame, Earth, 0.2, 0.3, 0.03, 0, 0)
# Earth = Point()

# EarthRef = ReferenceFrame() #need to pass epoch!

# create 3 satellites

# orbit stuff
# define earth orbit

# define satellite orbit?
