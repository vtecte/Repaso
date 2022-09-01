from abc import ABC, abstractmethod
from math import radians
from random import choice, randint, random
from unidades import Guerrero, Mago, MagoGuerrero
from parametros import PROB_CRITICO_MURO, PROB_CRITICO_CATAPULTA, \
                       HP_MUROCATAPULTA, PROB_CRITICO_MURO_CATAPULTA, \
                       HP_BARRACAS, HP_MURO, HP_CATAPULTA


# Recuerda que es una clase abstracta
class Estructura(ABC):

    def __init__(self, edad, *args):
        # No modificar
        super().__init__(*args)
        self.edad = edad
        self.asignar_atributos_segun_edad()

    # ---------------
    # Completar los métodos abstractos aquí
    @abstractmethod
    def asignar_atributos_segun_edad(self):
        pass
    
    @abstractmethod
    def accion(self):
        pass

    @abstractmethod
    def avanzar_edad(self):
        pass
    # ---------------


# Recuerda completar la herencia
class Barracas(Estructura):

    def __init__(self, *args):
        # Completar
        super().__init__(*args)
        self.hp = HP_BARRACAS

    # ---------------
    # Completar los métodos aquí
    def asignar_atributos_segun_edad(self):
        if self.edad == 'Media':
            self.unidades = ['Guerrero', 'Mago']
        elif self.edad == 'Moderna':
            self.unidades = ['Guerrero', 'Mago', 'MagoGuerrero' ]

    
    def avanzar_edad(self):
        if self.edad == 'Media':
            self.edad = 'Moderna'
            self.unidades.append('MagoGuerrero')
    # ---------------

    def accion(self):
        # No modificar
        elegido = choice(self.unidades)
        suerte = choice((True, False))
        experiencia = choice([1, 2, 3, 4, 5, 6])
        energia = choice([1, 2, 3, 4, 5, 6])
        if elegido == "Guerrero":
            return elegido, Guerrero(suerte, xp=experiencia, stamina=energia)
        elif elegido == "Mago":
            return elegido, Mago(suerte, xp=experiencia, stamina=energia)
        elif elegido == "MagoGuerrero":
            atributos = {"bendito": suerte, "armado": suerte, "xp": experiencia,
                         "stamina": energia}
            return elegido, MagoGuerrero(**atributos)


# Recuerda completar la herencia
class Muro(Estructura):

    def __init__(self, *args):
        # Completar
        super().__init__(*args)
        self.hp = HP_MURO
    # ---------------
    # Completar los métodos aquí
    def asignar_atributos_segun_edad(self):
        if self.edad == 'Media':
            self.reparacion = [20, 80]
        elif self.edad == 'Moderna':
            self.reparacion = [40, 100]
    

    def accion(self):
        if randint(1,100) < PROB_CRITICO_MURO:
            return 2 * randint(self.reparacion[0], self.reparacion[1])
        return randint(self.reparacion[0], self.reparacion[1])
    
    
    def avanzar_edad(self):
        if self.edad == 'Media':
            self.edad = 'Moderna'
            self.reparacion = [40, 100]
    # ---------------


# Recuerda completar la herencia
class Catapulta(Estructura):

    def __init__(self, *args):
        # Completar
        super().__init__(*args)
        self.hp = HP_CATAPULTA
    # ---------------
    # Completar los métodos aquí
    def asignar_atributos_segun_edad(self):
        if self.edad == 'Media':
            self.ataque = [40, 100]
        elif self.edad == 'Moderna':
            self.ataque = [80, 140]

    def accion(self):
        if randint(1,100) < PROB_CRITICO_CATAPULTA:
            return 2 * randint(self.ataque[0], self.ataque[1])
        return randint(self.ataque[0], self.ataque[1])

    def avanzar_edad(self):
        if self.edad == 'Media':
            self.edad = 'Moderna'
            self.ataque = [80, 140]
    # ---------------


# Recuerda completar la herencia
class MuroCatapulta(Muro, Catapulta):

    def __init__(self, *args):
        # Completar
        super().__init__(*args)
    # ---------------
    # Completar los métodos aquí
    def asignar_atributos_segun_edad(self):
        return super().asignar_atributos_segun_edad()
    

    def accion(self):
        if randint(1, 100) < PROB_CRITICO_MURO_CATAPULTA:
            
            return (round(2.5*randint(self.reparacion[0], self.reparacion[1])),
                           round(2.5*randint(self.ataque[0], self.ataque[1])))
        return (randint(self.reparacion[0], self.reparacion[1]),
                        randint(self.ataque[0], self.ataque[1]))
            

    def avanzar_edad(self):
        if self.edad == 'Media':
            self.edad = 'Moderna'
            self.reparacion = [40, 100]
            self.ataque = [80, 140]
    # ---------------
    
if __name__ == "__main__":
    # ---------------
    # En esta sección puedes probar tu codigo
    # ---------------
    pass
