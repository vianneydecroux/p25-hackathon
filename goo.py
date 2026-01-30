import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

x_min = -50
x_max = 50
y_min = -50
y_max = 50

g=9.81/20
k=100
dt=1
Liste_goos = []  #vecteur de goos

class goo:
    def __init__(self, x, y, pl):
        g=9.81/20
        self.plateforme = pl               #true -> plateforme et pas goo
        self.position = np.array([x,y])
        self.mass = 0.4
        self.rayon = 0.01
        self.vitesse = np.array([0,0])
        self.forces = np.array([0,-self.mass*g]) #liste force x et force y
        self.liens = {}  #entrée liens sortie l0
        for g in Liste_goos:
            l = np.sqrt( (self.position[0]-g.position[0])**2 + (self.position[1]-g.position[1])**2 )
            if  l <= 20 and not(g.plateforme):
                self.liens[g] = l
            if  l <= 10 and g.plateforme:
                self.liens[g] = l
    
    def update_forces(self):
        for b in self.liens.keys:
            d=np.sqrt(d_x**2+d_y**2)
            d_x=self.position[0]-b.position[0]
            d_y=self.position[1]-b.position[1]
            self.force[0]+=-k(d-self.liens[b])*d_x/d
            self.force[1]+=-k(d-self.liens[b])*d_y/d

        if not(self.plateforme):
            for g in Liste_goos:
                l = np.sqrt( (self.position[0]-g.position[0])**2 + (self.position[1]-g.position[1])**2 )
                if l==0: Liste_goos.pop(self)
                if  l <= 20 and not(g.plateforme):
                    self.liens[g] = l
                if  l <= 10 and g.plateforme:
                    self.liens[g] = l
            if self.liens=={}: Liste_goos.pop(self)

    

<<<<<<< HEAD
=======
"""Pour travailler directement sur les forces"""
N = 3
x_min, x_max = -10., 10.
y_min, y_max = -10., 10.
speed_max = 1

X = np.random.uniform(x_min,x_max,N)
Y = np.random.uniform(y_min,y_max,N)
VX = np.random.uniform(0,speed_max,N)
VY = np.random.uniform(0,speed_max,N)

<<<<<<< HEAD
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
            d=np.sqrt(d_x**2+d_y**2)
            d_x=a.position[0]-b.position[0]
            d_y=a.position[1]-b.position[1]
            a.force[0]+=-k(d-a.liens[b])*d_x/d
            a.force[1]+=-k(d-a.liens[b])*d_y/d-a.mass*g
=======
>>>>>>> b2ef091dbb66718d12efac9d9718ab615557b5d8



<<<<<<< HEAD
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
=======
fig, ax = plt.subplots()
ax.set(xlim=[x_min,x_max],ylim=[y_min,y_max])
pos=[]
for goo in Liste_goos:
    pos.append([goo.position[0],goo.position[1]])
pos=np.array(pos)
scat = ax.scatter(pos[:,0],pos[:,1],s=1)

>>>>>>> 87ec2e0f540190dd69282ccdfc0d38c2e7b48998

def tdt(t):
    pos_x=[]
    pos_y=[]
    global Liste_goos 
    for goo in Liste_goos :
        if goo.plateforme!=True:
            goo.vitesse[0] = goo.vitesse[0] + dt*goo.forces[0]
            goo.vitesse[1] = goo.vitesse[1] + dt*goo.forces[1]
            goo.position[0] = goo.position[0] +dt*goo.vitesse[0]
            goo.position[1] = goo.position[1] +dt*goo.vitesse[1]
            goo.update_forces()
            pos_x.append(goo.position[0])
            pos_y.append(goo.position[1])
    scat.set_offsets(np.transpose([pos_x,pos_y]))
    return scat


"""Initialisation des plateformes"""
for i in range (0,20,1):
    Liste_goos.append(goo(x_min + i,0,True))
    Liste_goos.append(goo(x_max - i,0,True))
Liste_goos.append(goo(x_min + 25,0,False))
<<<<<<< HEAD
Liste_goos.append(goo(x_min + 30,0,False))

fig, ax = plt.subplots()
ax.set(xlim=[x_min,x_max],ylim=[y_min,y_max])
pos_x=[]
pos_y=[]
for goo in Liste_goos:
    pos_x.append(goo.position[0])
    pos_y.append(goo.position[1])
scat = ax.scatter(pos_x,pos_y,s=30)
ani = animation.FuncAnimation(fig = fig, func=tdt, interval=100)
plt.show()
=======
Liste_goos.append(goo(x_min + 40,0,False))
>>>>>>> b2ef091dbb66718d12efac9d9718ab615557b5d8
>>>>>>> 87ec2e0f540190dd69282ccdfc0d38c2e7b48998
