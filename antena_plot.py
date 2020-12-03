#Exercícios Massimo - Tabata

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import cm

L = 5e9/3e8 #segundos
psi = 0
f = 1 #Hz
w = 2*np.pi*f
A = 1

def F_mais_oneway(phi, theta):
	return ((1 + np.cos(theta))/2)*(A*np.cos(2*phi)*(np.cos(w*L) - np.cos(w*np.cos(theta)*L)) + A*np.sin(2*phi)*(np.sin(w*np.cos(theta)*L) - np.sin(w*L)))


def F_cruzado_oneway(phi, theta):
	return ((1 + np.cos(theta))/2)*(A*np.cos(2*phi)*(np.sin(w*L) - np.sin(w*np.cos(theta)*L)) + A*np.sin(2*phi)*(np.cos(w*L)- np.cos(w*np.cos(theta)*L)))


def F_mais_LIGO(phi, theta, psi):
	return 0.5*(1+ np.cos(theta)*np.cos(theta))*np.cos(2*phi)*np.cos(2*psi) -np.cos(theta)*np.np.sin(2*phi)*np.np.sin(2*psi)


def F_cruzado_LIGO(phi, theta, psi):
	return (-0.5)*(1+ (np.cos(theta)*np.cos(theta))*np.cos(2*phi)*np.np.sin(2*psi)) - (np.cos(theta)*np.np.sin(2*phi)*np.cos(2*psi))


phi, theta = np.mgrid[-np.pi:np.pi:5000j, 0:np.pi:5000j]



z_mais = F_mais_oneway(phi,theta)
z_cruzado = F_cruzado_oneway(phi,theta)


#plot F. theta, phi
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(phi, theta,z_mais,color='b')
ax.plot_surface(phi, theta,z_cruzado,color='g')
ax.set_xlabel('phi')
ax.set_ylabel('theta')
ax.set_zlabel('F+')


#Plot x, y e z
fig = plt.figure()
ax = fig.gca(projection='3d')

x_mais= abs(z_mais)*np.sin(theta)*np.cos(phi)
y_mais= abs(z_mais)*np.sin(theta)*np.sin(phi)
z_mais = abs(z_mais)*np.cos(theta)

x_cruzado= abs(z_cruzado)*np.sin(theta)*np.cos(phi)
y_cruzado= abs(z_cruzado)*np.sin(theta)*np.sin(phi)
z_cruzado = abs(z_cruzado)*np.cos(theta)

ax.plot_surface(x_mais,y_mais,z_mais,color='b')
ax.plot_surface(x_cruzado,y_cruzado,z_cruzado,color='g')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')


