# thickness distribution

import numpy as np
from scipy.interpolate import interp1d


upper = np.array([0.000000,  0.000000, 0.004300,  0.008760, 0.006690,  0.011070, 0.011620,  0.013790, 0.023980,
                 0.019390, 0.048860,  0.027530, 0.073820,  0.033720, 0.098820,  0.038770, 0.148900,  0.046650, 0.199020,
                 0.052400, 0.249170,  0.056470, 0.299330,  0.059100, 0.349510,  0.060300, 0.399680,  0.060090, 0.449850,
                 0.058610, 0.500000,  0.055990, 0.550130,  0.052350, 0.600240,  0.047860, 0.650320,  0.042640, 0.700360,
                 0.036840, 0.750380,  0.030610, 0.800360,  0.024140, 0.850300,  0.017610, 0.900210,  0.012120, 0.950100,
                 0.005300, 1.000000,  0.000000])

x_up = upper[::2]
y_up = upper[1::2]

lower = np.array([0.000000, 0.000000, 0.005700, -0.007760, 0.008310, -0.009670, 0.013380, -0.011650, 0.026020,
                  -0.015670, 0.051140, -0.021210, 0.076180, -0.025240, 0.101180, -0.028430, 0.151100, -0.033190,
                  0.200980, -0.036480, 0.250830, -0.038570, 0.300670, -0.039660, 0.350490, -0.039700, 0.400320,
                  -0.038670, 0.450150, -0.036710, 0.500000, -0.033930, 0.549870, -0.030450, 0.589760, -0.026440,
                  0.649680, -0.022040, 0.699640, -0.017400, 0.749620, -0.012710, 0.799640, -0.008220, 0.849700,
                  -0.004150, 0.899790, -0.000870, 0.949900,  0.001200, 1.000000,  0.000000])

x_low = lower[::2]
y_low = lower[1::2]

h_up = interp1d(x_up, y_up)
h_low = interp1d(x_low, y_low)

def airfoil_surface(x):
    """Returns upper and lower coordinate of airfoil surface for a chordwise posistion"""
    return h_up(x), h_low(x)

def thickness(x):
    y1 = h_up(x)
    y2 = h_low(x)
    t = y1 - y2
    return t
