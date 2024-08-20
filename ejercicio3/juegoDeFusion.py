"""
Crea un juego de fusión.
El juego consiste en crear personajes un juego y que esos personajes se
puedan fusionar para formar personajes más poderosos que tengan más poder.
Para ello debemos cambiar el comportamiento del operador "+"
para que cuando los personajes se fusionen,
salga un nuevo personaje con habilidades mejoradas.
Una posible formual es:
El promedio de las habilidades en ambos, al cuadrado
"""

from abc import ABC, abstractclassmethod
from math import sqrt

def formula(number: int):
    valor = sqrt((number/2))
    return valor

class Personaje(ABC):
    def __init__(self, nivel: int, vida: int, nombreEsp: str, puntosEsp :int) -> None:
        self.__nivel = nivel
        self.__vida = vida
        self.__nombreEsp = nombreEsp
        self.__puntosEsp = puntosEsp
        
     #Inicia Nivel   
    @property    
    def nivel(self):
        return self.__nivel
    
    @nivel.setter
    def nivel(self, nivel):
        self.__nivel = nivel
        
    @nivel.deleter
    def nivel(self):
        del self.__nivel
    #Fin nivel
    #Inicia vida
    @property    
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, vida):
        self.__vida = vida
        
    @vida.deleter
    def vida(self):
        del self.__vida
    #Fin vida
    #Inicia nombreEsp
    @property        
    def nombreEsp(self):
        return self.__nombreEsp
    
    @nombreEsp.setter
    def nombreEsp(self, nombreEsp):
         self.__nombreEsp = nombreEsp
         
    @nombreEsp.deleter     
    def nombreEsp(self):
        del self.__nombreEsp
    #Fin NombreEsp
    #Inicia puntosEsp
    @property        
    def puntosEsp(self):
        return self.__puntosEsp
    
    @puntosEsp.setter
    def puntosEsp(self, puntosEsp):
         self.__puntosEsp = puntosEsp
         
    @puntosEsp.deleter     
    def puntosEsp(self):
        del self.__puntosEsp
    #Fin puntosEsp
    
    def __add__(self, other):
        vidaFusion = self.__vida + other.__vida
        nivelFusion = self.__nivel + other.__nivel
        puntosFusion = self.__puntosEsp + other.__puntosEsp
        nombreFusion = f"{self.__nombreEsp} y {other.__nombreEsp}"
        return Personaje(nivelFusion, vidaFusion, nombreFusion, puntosFusion)
    
juan = Personaje(30, 1000, "fuerza", 50)
pedro = Personaje(50, 2000, "magia", 80)
maria = Personaje(70, 3000, "rapidez", 90)

nueva_persona = juan + pedro + maria
print(nueva_persona.nombreEsp)