#Raghu Alluri
#May 2021
"""Hydrogen 1s Orbital Depiction"""

import matplotlib.pyplot as mpt
import numpy as np

pos = np.linspace(0,1,50)

R3 = []
P_values = []

def P(x,y,z):
    r = np.sqrt(x**2 + y**2 + z**2)
    P = pow(np.exp(-r)/np.sqrt(np.pi),2)

    return P

x_pos, y_pos, z_pos = pos, pos, pos

for x in x_pos:
    for y in y_pos:
        for z in z_pos:
            R3.append(str((x,y,z)))
            P_values.append(P(x,y,z))

#Now to "normalize" such that sum of all P's are 1, with the commented section being a way to do it.
"""sum_P = sum(P_values)
for i in range(len(P_values)):
    P_values[i] = P_values[i]/sum_P"""

P_values = P_values / sum(P_values)

vectors = np.random.choice(R3, size=100000, replace=True, p=P_values)

R3_matrix = []
for i in vectors:
    R3_matrix.append(i.split(','))
    
R3_matrix = np.matrix(R3_matrix)

x_components = []
for j in R3_matrix[:,0]:
    x_components.append(float(j.item()[1:]))

y_components = []
for k in R3_matrix[:,1]:
    y_components.append(float(k.item()))

z_components = []
for l in R3_matrix[:,2]:
    z_components.append(float(l.item()[0:-1]))

plot = mpt.figure()
basis = plot.add_subplot(projection='3d')
basis.scatter(x_components, y_components, z_components, alpha=0.04, s=1)
basis.set_title("Plot of Probability Density \n(Modulus Squared of Wave Function) for Hydrogen 1s Orbital")
mpt.show()


































