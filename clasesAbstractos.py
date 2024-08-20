from abc import ABC, abstractclassmethod

#Esto pasa a ser una plantilla
class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad) -> None:
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    @abstractclassmethod    
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} años")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")
        
class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print(f"Actualmente estoy trabajando en el rubro de: {self.actividad}")
        

dylan = Estudiante("dylan", 25, "Masculino", "Programación")
lucas = Trabajador("lucas", 21, "Masculino", "Programación")

dylan.hacer_actividad()
lucas.hacer_actividad()
        
