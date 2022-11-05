
class weapon :
    def __init__(self, ammunitions : int, rang : int) :
        self.ammunitions=ammunitions
        self.rang=rang
    
        def fire_at(self, x: int, y: int, z: int):
            self.x=x
            self.y=y
            self.z=z
            print("x: {self._x}, y: {self._y}, z: {self._z}")
 

class Lance_missiles_antisurface (weapon):
    def __init__(self,ammunitions : int, rang : int):
        self.ammunitions = 30
        self.rang = 40
      

    def fire_at(self, x, y, z):
        if self.ammunitions ==0 :
            print( "NoAmmunitionError")
        elif z !=0 :
            print("OutOfRangeError")
            self.ammunitions = self.ammunitions - 1



class Lance_missiles_anti_air(weapon):
    def __init__(self, ammunitions: int, rang: int):
        self.ammunitions = 50
        self.rang = 40
    def fire_at(self, x, y, z):
        if self.ammunitions ==0 :
            print( "NoAmmunitionError")
        elif z<=0 :
            print("OutOfRangeError")
            self.ammunitions = self.ammunitions -1



class Lance_tropille(weapon):
    def __init__(self, ammunitions: int, rang: int):
        self.ammunitions = 15
        self.rang = 20

    def fire_at(self,ammunitions: int, x: int, y: int, z: int):
        if ammunitions ==0 :
            print( "NoAmmunitionError")
        if z>0 :
            print("OutOfRangeError")
            self.ammunitions = self.ammunitions-1
        else:
            super().fire_at(x,y,z)
