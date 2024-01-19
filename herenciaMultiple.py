class Persona:
    def __init__(self, nombre: str, edad: int, nacionalidad: str):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print("Hola, estoy hablando un poco")
        
class Artista:
    def __init__(self, habilidad: str):
        self.habilidad = habilidad
        
    def mostrarHabilidad(self):
        return f"Mi habilidad es: {self.habilidad}"
        
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre: str, edad: int, nacionalidad: str, habilidad: str, salario: float, empresa: str):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        #Forma de llamar a una clase según la documentación
        #class C(B):
        #    def method(self, arg):
        #    super().method(arg)
            # This does the same thing as:
            # super(C, self).method(arg)
        #super(Artista, self).__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
    
    #Formas de llamar un método de un superclase    
    def presentarase(self):
        #print(f"{self.mostrarHabilidad()}")
        #return f"{self.mostrarHabilidad()}"
        #return Artista.mostrarHabilidad(self)
        return f'Hola, soy {self.nombre}, {super().mostrarHabilidad()} y trabajo en {self.empresa}'
        
        
roberto = EmpleadoArtista("Roberto", 43, "Argentino", "Programador", 100000, "Dingo")
diego = Artista("Cirujano")

print(roberto.presentarase())

#Tupla de objetos de clase
tuplaPersona = (Persona, )
print(issubclass(EmpleadoArtista, tuplaPersona)) #True
#Retorna True, si class es una subclase de classinfo
herencia = issubclass(Artista, Persona)
print(herencia) #False
herencia = issubclass(EmpleadoArtista, Persona)
print(herencia) #True

#Retorna True, si Object(Roberto) es una instancia de la clase EmpleadoArtista
instancia = isinstance(roberto, EmpleadoArtista)
print(instancia) #True
#Retorna True, si Object(Roberto) es una instancia que hereda cualidades de Persona que lo contiene la clase EmpleadoArtista
instancia = isinstance(roberto, Persona)
print(instancia) #True
#Retorna True, si Object(Diego) es una instancia de la clase EmpleadoArtista
instancia = isinstance(diego, EmpleadoArtista) 
print(instancia) #False



