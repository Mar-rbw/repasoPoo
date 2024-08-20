class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self) -> str:
        return f"Persona(nombre={self.nombre}, edad={self.edad})"
    
    def __repr__(self) -> str: #Representacion de la clase
        return f"Persona('{self.nombre}', {self.edad})"
    
    #sobrecarga de operadores
    def __add__(self, otro):
        nuevoValor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre, nuevoValor)
    
    
    
juan = Persona("Juan", 21)
pedro = Persona("Pedro", 20)
maria = Persona("Maria", 18)

print(juan) # contenido de _str_
repre = repr(juan)
resultado = eval(repre) #Es el resultado
print(repre) #Persona('lucas', 21)
print(resultado)#Persona(nombre=lucas, edad=21)

nueva_persona = juan + pedro + maria
print(nueva_persona.edad)

