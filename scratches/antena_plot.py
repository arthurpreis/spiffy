#Exercícios Massimo - Tabata
import mayavi.mlab as mlab
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import cm

L = 5e9/3e8 #segundos
psi = 0
f = .001 #Hz
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

phi, theta = np.mgrid[-np.pi:np.pi:100j, 0:np.pi:100j]
print(phi)
print(theta)
z_mais = F_mais_oneway(phi,theta)
z_cruzado = F_cruzado_oneway(phi,theta)

x_mais= abs(z_mais)*np.sin(theta)*np.cos(phi)
y_mais= abs(z_mais)*np.sin(theta)*np.sin(phi)
z_mais = abs(z_mais)*np.cos(theta)

x_cruzado= abs(z_cruzado)*np.sin(theta)*np.cos(phi)
y_cruzado= abs(z_cruzado)*np.sin(theta)*np.sin(phi)
z_cruzado = abs(z_cruzado)*np.cos(theta)
print(x_cruzado.shape)
mlab.mesh(x_cruzado,y_cruzado,z_cruzado)
mlab.show()
