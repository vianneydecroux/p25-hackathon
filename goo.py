import numpy as np
import matplotlib.pyplot as plt

x_min = -10
x_max = 10
y_min = -10
y_max = 10
N = 3
speed_max = 1

L = []

class goo:
    def __init__(self, x, y):
        self.position = np.array([x,y])
        self.mass = 0.4
        self.rayon = 0.01
        self.vitesse = np.array([0,0])
        self.force = np.array([0,0]) #liste force x et force y
        self.liens = {}  #entrée liens sortie l0
        for g in L:
            l = np.sqrt( (self.position[0]-g.position[0])**2 + (self.position[1]-g.position[1])**2 )
            if  l <= 20:
                self.liens[g] = l
        

    

"""Pour travailler directement sur les forces"""

X = np.random.uniform(x_min,x_max,N)
Y = np.random.uniform(y_min,y_max,N)
VX = np.random.uniform(0,speed_max,N)
VY = np.random.uniform(0,speed_max,N)
    
positions = np.concatenate((X,Y)).reshape(2,N)
speeds = np.concatenate((VX,VY)).reshape(2,N)

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



pl1 = np.array([x_min,1,x_min+3,-1])
pl2 = np.array([x_max-2,3,x_max,-1])

