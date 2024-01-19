class Persona:
    def __init__(self, nombre: str, edad: int, nacionalidad: str):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print("Hola, estoy hablando un poco")
        
class Empleado(Persona):
    def __init__(self, nombre: str, edad: int, nacionalidad: str, trabajo: str, salario: float):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
    #La herencia permite sobreescribir las funciones    
    def hablar(self):
        print("Hola, estoy hablando mucho")

class Estudiante(Persona):
    def __init__(self, nombre: str, edad: int, nacionalidad: str, notas: float, universidad: str):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad


roberto = Empleado("Roberto", 43, "Argentino", "Programador", 100000)

roberto.hablar()