class OutOfRangeError(Exception):
    pass

class NoAmmunitionError(Exception):
    pass

class weapon :
    def __init__(self, ammunitions : int, rang : int) :
        self.ammunitions=ammunitions
        self.rang=rang
    def fire_at(self, x: int, y: int, z: int):
        if self.ammunitions != 0 :
            self.ammunitions = self.ammunitions-1
        else :
            raise NoAmmunitionError


class Lance_missiles_antisurface (weapon):
    def __init__(self):
        self.ammunitions = 30
        self.rang = 40
    def fire_at(self, x: int, y: int,z : int):
        if z == 0:
            if self.ammunitions != 0 :
                self.ammunitions = self.ammunitions-1
            else :
                raise NoAmmunitionError
        else :
            raise OutOfRangeError



class Lance_missiles_anti_air(weapon):
    def __init__(self):
        self.ammunitions = 50
        self.rang = 40

    def fire_at(self, x: int, y: int, z: int):
        if z > 0:
            if self.ammunitions != 0:
                self.ammunitions = self.ammunitions - 1
            else:
                raise NoAmmunitionError
        else:
            raise OutOfRangeError



class Lance_tropille(weapon):
    def __init__(self):
        self.ammunitions = 15
        self.rang = 20

    def fire_at(self, x: int, y: int, z: int):
        if z <= 0:
            if self.ammunitions != 0:
                self.ammunitions = self.ammunitions - 1
            else:
                raise NoAmmunitionError
        else:
            raise OutOfRangeError