import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backend_bases import MouseButton

éta=1
x_min = -0.50
x_max = 0.50
y_min = -0.50
y_max = 0.50

g=9.81/20
k=100
dt=0.01
liste_goos = []  #vecteur de goos

class Goo:
    def __init__(self, x, y, pl):
        self.plateforme = pl               #true -> plateforme et pas goo
        self.position = np.array([x,y], dtype = float)
        self.mass = 0.4
        self.rayon = 0.01
        self.vitesse = np.array([0,0], dtype = float)
        self.forces = np.array([0,-self.mass*g], dtype = float) #liste force x et force y
        self.liens = {}  #entrée liens sortie l0
        self.Prob = False
        if not(self.plateforme):
            for go in liste_goos:
                l = np.sqrt( (self.position[0]-go.position[0])**2 + (self.position[1]-go.position[1])**2 )
                if l==0: self.Prob = True
                if  l <= 0.20 and not(go.plateforme):
                    self.liens[go] = l
                    go.liens[self] = l
                if  l<= 0.10 and go.plateforme:
                    self.liens[go] = l
            if self.liens=={}: self.Prob = True
    
    def update_forces(self):
        self.forces=np.array([0,-self.mass*g])
        for b in self.liens.keys():
            d_x=self.position[0]-b.position[0]
            d_y=self.position[1]-b.position[1]
            d=np.sqrt(d_x**2+d_y**2)
            self.forces[0]+=-k*(d-self.liens[b])*d_x/(d+0.01)
            self.forces[1]+=-k*(d-self.liens[b])*d_y/(d+0.01)

def on_click(event):
    if event.button is MouseButton.LEFT:
        print(1)
        x,y=(event.xdata,event.ydata)
        liste_goos.append(Goo(x,y,False))
        if liste_goos[-1].Prob:
            liste_goos.pop()
        else:
            go = liste_goos[-1]
            for go2 in go.liens.keys():
                line, = ax.plot([go.position[0], go2.position[0]], [go.position[1], go2.position[1]], c= 'b')
                lines.append((line, go, go2))
        



def tdt(t):
    pos=[]
    global liste_goos 
    for go in liste_goos :
        if go.plateforme!=True:
            go.vitesse[0] = go.vitesse[0] + dt*(go.forces[0]-éta*go.vitesse[0])/go.mass
            go.vitesse[1] = go.vitesse[1] + dt*(go.forces[1]-éta*go.vitesse[1])/go.mass
            go.position[0] = go.position[0] +dt*go.vitesse[0]
            go.position[1] = go.position[1] +dt*go.vitesse[1]
            go.update_forces()
        pos.append([go.position[0],go.position[1]])
    pos= np.array(pos)
    scat.set_offsets(pos)
    for line, go, go2 in lines:
        line.set_data([go.position[0], go2.position[0]], [go.position[1], go2.position[1]])

    return scat, *[l[0] for l in lines]



"""Initialisation des plateformes"""
for i in range (21):
    liste_goos.append(Goo(x_min + i*0.01,0,True))
    liste_goos.append(Goo(x_max - i*0.01,0,True))
liste_goos.append(Goo(x_min + 0.3,0,False))
if liste_goos[-1].Prob:
    liste_goos.pop()
liste_goos.append(Goo(x_min + 0.40,0,False))
if liste_goos[-1].Prob:
    liste_goos.pop()

fig, ax = plt.subplots()
ax.set(xlim=[x_min,x_max],ylim=[y_min,y_max])
pos_x=[]
pos_y=[]
for go in liste_goos:
    pos_x.append(go.position[0])
    pos_y.append(go.position[1])

scat = ax.scatter(pos_x,pos_y,s=30)
lines = []
for go in liste_goos :
    for go2 in go.liens.keys():
        line, = ax.plot([go.position[0], go2.position[0]], [go.position[1], go2.position[1]], c= 'b')
        lines.append((line, go, go2))

ani = animation.FuncAnimation(fig = fig, func=tdt, frames = 10000, interval=1)


plt.connect('button_press_event', on_click)
plt.show()
