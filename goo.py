import numpy as np
import matplotlib.pyplot as plt



"""Pour travailler directement sur les forces"""
N = 3
x_min, x_max = -10., 10.
y_min, y_max = -10., 10.
speed_max = 1

X = np.random.uniform(x_min,x_max,N)
Y = np.random.uniform(y_min,y_max,N)
VX = np.random.uniform(0,speed_max,N)
VY = np.random.uniform(0,speed_max,N)
    
positions = np.concatenate((X,Y)).reshape(2,N)
speeds = np.concatenate((VX,VY)).reshape(2,N)

dict = {0:[(1,3),(2,3)],1:[(0,3)],2:[(0,3)]}


def forces(position,dict):






class goo:
    def __init__(self, x, y):
        self.position = np.array([x,y])
        self.mass = 0.4
        self.rayon = 0.01
        self.vitesse = np.array([0,0])
        self.force = np.array([0,])
        self.liens = dict{}
            

    def ajouter_force()

def forces(a,vector_goos):
    for b in vector_goos:
        if b in a.liens.key:
            d_x=a.position[0]-b.position[0]
            d_y=a.position[1]-b.position[1]
            a.force[0]+=-k(d_x-a.liens[b])
            a.force[1]+=-k(d_y-a.liens[b])-a.mass*g

a = goo(X[0],Y[0])
L.append(a)
L.append(b)
b = goo(X[1],Y[1])


def forces(a , b):
    if b in a.liens.key:
        d_x=a.position[0]-b.position[0]
        d_y=a.position[1]-b.position[1]
        a.force[0]=-k(dx-a.liens[b])
        a.force[1]=-k(dy-a.liens[b])-a.mass*g

pl1 = np.array([x_min,1,x_min+3,-1])
pl2 = np.array([x_max-2,3,x_max,-1])