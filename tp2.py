from tp1 import weapon

class vessel:
    def __init__(self,coordinates:tuple,max_hits:int,W:weapon):
        self.coordinates=coordinates
        self.max_hits=max_hits
        self.W=W
    
    def get_coordinates(self):
        return self.coordinates
    def go_to(self,x,y,z):
        self.coordinates=(x,y,z)
    def fire_at(self,x,y,z):
        if self.max_hits==0:
            raise IndexError('DestroyedError')
        if ((x-self.coordinates[0])**2+(y-self.coordinates[1])**2+(z-self.coordinates[2])**2)**(1/2)>self.W.rang:
            print(self.W)
            self.W.ammunitions-=1
            raise IndexError('OutOfRangeError')
            


class Cruisier(vessel):
    def __init__(self,x,y):
        self.coordinates=(x,y,0)
        self.max_hits=6
        self.W=Lance_missiles_anti_air()
    def go_to(self,x,y,z):
        self.coordinates=(x,y,0)

class Submarine(vessel):
    def __init__(self,x,y,z):
        if z==0 or z==-1:
            self.coordinates=(x,y,z)
            self.max_hits=2
            self.W=Lance_tropille()
        else:
            raise IndexError('z=0 or z=-1')
    def go_to(self,x,y,z):
        if z==0 or z==-1:
            self.coordinates=(x,y,z)
        else:
            raise IndexError('z=0 or z=-1')

class fregate(vessel):
    def __init__(self,x,y):
        self.coordinates=(x,y,0)
        self.max_hits=5
        self.W=Lance_missiles_antisurface()
    def go_to(self,x,y,z):
            self.coordinates=(x,y,0)


class Destroyer(vessel):
    def __init__(self,x,y):
        self.coordinates=(x,y,0)
        self.max_hits=4
        self.W=Lance_tropille()
    def go_to(self,x,y,z):
        self.coordinates=(x,y,0)

class Aircraft(vessel):
    def __init__(self,x,y):
        self.coordinates=(x,y,1)
        self.max_hits=1
        self.W=Lance_missiles_antisurface()
    def go_to(self,x,y,z):
        self.coordinates=(x,y,1)

class espace:
    def __init__(self,x:int,y:int,z:int, vaisseaux: list):
        if 0<=y<=100 and (z==1 or z==0 or z==-1):
            self.x=x
            self.y=y 
            self.z=z
            self.vaisseaux=vaisseaux
        else:
            raise IndexError('z doit appartenir à {1,0,-1} et y compris entre 0 et 100')

    def ajoutervaisseaux(self,vaisseau:vessel):
        s=0
        for i in self.vaisseaux:
            s+=i.max_hits
        for i in self.vaisseaux:
            if i.coordinates!=vaisseau.coordinates and s<=22:
                self.vaisseaux.append(vaisseau)
    def recevoir(self,x,y,z):
        for e in self.vaisseaux:
            if e.coordinates==(x,y,z):
                return True
            else:
                return False


a=weapon(30,40)
a.fire_at(0,0,0)
b=Lance_missiles_antisurface()
b.fire_at(0,0,0)
c=Lance_missiles_anti_air()
c.fire_at(0,0,1)
d=Lance_tropille()
d.fire_at(0,0,-2)
e=Cruisier(1,1)
e.go_to(1,1,1)
#e.fire_at(100,100,100)
f=fregate(2,3)
f.go_to(1,5,1)
f.fire_at(1,1,1)
A=espace(1,2,1,[e])
A.ajoutervaisseaux(f)
print(A.vaisseaux)
A.recevoir(2,3,0)
d=Destroyer(4,5)
print(d.coordinates)
#d=Submarine(5,6,9)
#print(d.coordinates)
a=Submarine(1,4,0)
b=Destroyer(2,5)
l=[a,b]
e=espace(16,45,1,[a,b])
e.ajoutervaisseaux(Aircraft(4,5))