from tp1 import weapon
from tp1 import Lance_missiles_antisurface
from tp1 import Lance_missiles_anti_air
from tp1 import Lance_tropille
from tp2 import vessel
from tp2 import Cruisier
from tp2 import fregate
from tp2 import Submarine
from tp2 import Destroyer
from tp2 import Aircraft
from tp2 import espace
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
e.fire_at(100,100,100)
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