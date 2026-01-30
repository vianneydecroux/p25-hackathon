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

dict = {0:[1,2],1:[0],2:[0]}

class goo:
    def __init__(self, x, y):
        self.position = np.array([x,y])
        self.mass = 0.4
        self.rayon = 0.01
        self.vitesse = np.array([0,0])
        self.force = np.array([0,0])
        self.liens = []
    
    def ajouter_force

