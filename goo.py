import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

g=9.81/20
k=100
dt=10*-6

class goo:
    def __init__(self, x, y, pl):
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

x_min = -50
x_max = 50
y_min = -50
y_max = 50
N = 3
speed_max = 1

Liste_goos = []  #vecteur de goos

def tdt(t):
    pos = []
    for goo in Liste_goos:
        if not goo.plateforme:
            goo.vitesse[0] += dt * goo.forces[0]
            goo.vitesse[1] += dt * goo.forces[1]
            goo.position[0] += dt * goo.vitesse[0]
            goo.position[1] += dt * goo.vitesse[1]
            goo.update_forces()
        pos.append([goo.position[0], goo.position[1]])

    scat.set_offsets(np.array(pos))
    return scat


N = 3
x_min, x_max = -10., 10.
y_min, y_max = -10., 10.
speed_max = 1

for i in range (20):
    Liste_goos.append(goo(x_min + i*0.1,0,True))
    Liste_goos.append(goo(x_max - i*0.1,0,True))
Liste_goos.append(goo(x_min + 25,0,False))
Liste_goos.append(goo(x_min + 40,0,False))

X = np.random.uniform(x_min,x_max,N)
Y = np.random.uniform(y_min,y_max,N)
VX = np.random.uniform(0,speed_max,N)
VY = np.random.uniform(0,speed_max,N)

fig, ax = plt.subplots()
ax.set(xlim=[x_min, x_max], ylim=[y_min, y_max])

pos = np.array([[goo.position[0], goo.position[1]] for goo in Liste_goos])
scat = ax.scatter(pos[:,0], pos[:,1], s=1)

ani = animation.FuncAnimation(fig, tdt, frames=200, interval=100)
plt.show()