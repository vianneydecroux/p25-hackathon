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
dt=10*-6
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
        for b in self.liens.keys():
            d_x=self.position[0]-b.position[0]
            d_y=self.position[1]-b.position[1]
            d=np.sqrt(d_x**2+d_y**2)
            self.forces[0]+=-k(d-self.liens[b])*d_x/d
            self.forces[1]+=-k(d-self.liens[b])*d_y/d

        if not(self.plateforme):
            for g in Liste_goos:
                l = np.sqrt( (self.position[0]-g.position[0])**2 + (self.position[1]-g.position[1])**2 )
                if l==0: Liste_goos.pop(self)
                if  l <= 20 and not(g.plateforme):
                    self.liens[g] = l
                if  l <= 10 and g.plateforme:
                    self.liens[g] = l
            if self.liens=={}: Liste_goos.pop(self)

def tdt(t):
    pos=[]
    global Liste_goos 
    for goo in Liste_goos :
        if goo.plateforme!=True:
            goo.vitesse[0] = goo.vitesse[0] + dt*goo.forces[0]
            goo.vitesse[1] = goo.vitesse[1] + dt*goo.forces[1]
            goo.position[0] = goo.position[0] +dt*goo.vitesse[0]
            goo.position[1] = goo.position[1] +dt*goo.vitesse[1]
            goo.update_forces()
            pos.append([goo.position[0],goo.position[1]])
    pos=np.array(pos)
    scat.set_offsets(pos)
    return scat

"""Initialisation des plateformes"""
for i in range (20):
    Liste_goos.append(goo(x_min + i*0.1,0,True))
    Liste_goos.append(goo(x_max - i*0.1,0,True))
Liste_goos.append(goo(x_min + 25,0,False))
Liste_goos.append(goo(x_min + 40,0,False))

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
