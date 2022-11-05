from weapon import Weapon
from weapon import LT
from weapon import LMAA
from weapon import LMAS
from vessel import Vessel
from vessel import Cruiser
from vessel import Fregate
from vessel import Submarine
from vessel import Destroyer
from vessel import Aircraft
from espace import Espace
a=Weapon(30,40)
a.fire_at(0,0,0)
b=LMAA()
b.fire_at(0,0,-1)
c=LT()
c.fire_at(0,0,1)
d=LMAS()
d.fire_at(0,0,5)
e=Cruiser(1,1)
e.go_to(1,1,1)
e.fire_at(100,100,100)
f=Fregate(2,3)
f.go_to(1,5,1)
f.fire_at(1,1,1)
A=Espace(1,2,1,[e])
A.ajouter(f)
print(A._listeV)
A.recevoircoup(2,3,0)
