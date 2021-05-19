#Raghu Alluri
#May 2021
"""Simulating and depicting quantum wave functions
and probablistic distribution of electrons in the
1s orbital for Hydrogen."""

import numpy as np
import matplotlib.pyplot as mpt

h = 6.62607004e-34 #Planck's constant in m^2*kg/s
m_e = 9.11e-31 #Mass of an electron in kg

x_pos = np.linspace(0, 1, 100) #list of x positions within region of V = 0

#Here are the functions for the wave function and the square of the wave function
# I chose the value of L to be 1 for simplicity

def wave_func(x, n):
    psi = np.sqrt(2/1)*np.sin(n*np.pi*x/1)

    return psi

def wave_func_squared(x, n):
    psi_squared = np.square(wave_func(x, n))

    return psi_squared

n = int(input("Enter an integer greater than or equal to 1: "))

wave_func_range = []
wave_func_squared_range = []

for x in x_pos:
    wave_func_range.append(wave_func(x, n))
    wave_func_squared_range.append(wave_func_squared(x, n))

mpt.plot(x_pos, wave_func_range)
mpt.xlabel("x position")
mpt.ylabel("Wave Function (Probability Amplitude)")
mpt.title("Quantum Wave Functon for n={}".format(n))
mpt.show()
























