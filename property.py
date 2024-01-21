class Persona:
    def __init__(self, nombre: str, edad: int):
        self.__nombre = nombre
        self. __edad = edad
    
    #Es un Decorador especial porque es un Decorador reservado.
    #Indica que la función es un getter, ya no es necesario usar los parentesis.
    @property    
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, newName: str):
        self.__nombre = newName
        
    @nombre.deleter
    def  nombre(self):
        del self.__nombre
        
jose = Persona("Jose", 21)

#GETTER
#nombre = jose.get_nombre()
nombre = jose.nombre
print(nombre)

#SETTER
jose.nombre = "Pepe"
nombre = jose.nombre
print(nombre)

#DELETER
del jose.nombre
jose.nombre = "Pudu"
nombre = jose.nombre
print(nombre)

print("Que haces?")