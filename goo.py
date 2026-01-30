import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backend_bases import MouseButton

#Constantes
éta=2
x_min = -0.50
x_max = 0.50
y_min = -0.50
y_max = 0.50

g=9.81/10
k=100
dt=0.01
liste_goos = []  #vecteur de goos

class Goo:
    def __init__(self, x, y, pl):
        self.plateforme = pl                                    #true -> c'est une plateforme
        self.position = np.array([x,y], dtype = float)
        self.mass = 0.4
        self.rayon = 0.01
        self.vitesse = np.array([0,0], dtype = float)
        self.forces = np.array([0,-self.mass*g], dtype = float) #liste force x et force y
        self.liens = {}                                         #les clés sont les autres goos liés et le contenu et la longueur à vide du ressort
        self.Prob = False                                       #variable problème : true si superposition de 2 goos où si aucun lien
        if not(self.plateforme):
            liste_plateforme = []
            liste_distance = []
            for go in liste_goos:
                l = np.sqrt( (self.position[0]-go.position[0])**2 + (self.position[1]-go.position[1])**2 )
                if l==0: self.Prob = True
                if  l <= 0.20 and not(go.plateforme):
                    self.liens[go] = l
                    go.liens[self] = l
                if  l<= 0.10 and go.plateforme:
                    liste_plateforme.append(go)
                    liste_distance.append(l)
            if len(liste_distance) > 0:
                i = liste_distance.index(min(liste_distance))      #Unicité de l'accroche à la plateforme
                self.liens[liste_plateforme[i]] = liste_distance[i]
            if self.liens=={}: self.Prob = True
    
    def update_forces(self):
        self.forces=np.array([0,-self.mass*g])
        casse = []
        for b in self.liens.keys():
            d_x=self.position[0]-b.position[0]
            d_y=self.position[1]-b.position[1]
            d=np.sqrt(d_x**2+d_y**2)
            if d > self.liens[b] + 0.03:                           #Si le ressort vibre trop, il se brise
                casse.append(b)
            else:
                self.forces[0]+=-k*(d-self.liens[b])*d_x/(d+0.01)
                self.forces[1]+=-k*(d-self.liens[b])*d_y/(d+0.01)
        for b in casse:
            if (self, b) in lines:
                lines[(self, b)].remove()
                del lines[(self, b)]
            if (b, self) in lines:
                lines[(b, self)].remove()
                del lines[(b, self)]
            self.liens.pop(b)
            b.liens.pop(self, None)

def on_click(event):                                                #Les clics pour faire apparaitre un nouveau goos
    global g
    if event.button is MouseButton.LEFT:
        print(1)
        x,y=(event.xdata,event.ydata)
        liste_goos.append(Goo(x,y,False))
        if liste_goos[-1].Prob:                                     #Si problème, on le supprime directement
            liste_goos.pop()
        else:
            go = liste_goos[-1]
            for go2 in go.liens.keys():
                line, = ax.plot([go.position[0], go2.position[0]], [go.position[1], go2.position[1]], c= 'b')
                lines[(go,go2)] = line
    if event.button is MouseButton.RIGHT:
        g = 1.1 * g
        



def tdt(t):                                                         #mise à jour
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
    for (go, go2), line in lines.items():                           #dessin des lignes
        line.set_data([go.position[0], go2.position[0]], [go.position[1], go2.position[1]])

    return scat, *[l[0] for l in lines]



#Initialisation des 2 plateformes
for i in range (100):
    liste_goos.append(Goo(x_min + i*0.001,0,True))
    liste_goos.append(Goo(x_max - i*0.001,0,True))

fig, ax = plt.subplots()
ax.set(xlim=[x_min,x_max],ylim=[y_min,y_max])
pos_x=[]
pos_y=[]
for go in liste_goos:
    pos_x.append(go.position[0])
    pos_y.append(go.position[1])

scat = ax.scatter(pos_x,pos_y,s=30)
lines = {}                                                      #Dictionnaire des lignes à tracer
for go in liste_goos :
    for go2 in go.liens.keys():
        line, = ax.plot([go.position[0], go2.position[0]], [go.position[1], go2.position[1]], c= 'b')
        lines[(go,go2)] = line

ani = animation.FuncAnimation(fig = fig, func=tdt, frames = 1, interval=1)


plt.connect('button_press_event', on_click)
plt.show()
