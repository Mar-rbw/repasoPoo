class Estudiante():
    def __init__(self, nombre:str, edad:int, grado:str):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print(f"el estudiante {self.nombre} está estudiando")
        
          
nombre: str = input("Ingresa tu nombre: ").capitalize()
edad = int(input("Ingresa tu edad: "))
grado: str = input("Ingresa tu grado: ").upper()
estudiante = Estudiante(nombre, edad, grado)

print(f"""Buscando estudiante...\n
      Datos del estudiante:\n
      \tNombre: {estudiante.nombre}\n
      \tEdad: {estudiante.edad}\n
      \tGrado: {estudiante.grado}\n
      """)

while True:
    estudiar = input("Ingresa las palabras 'estudiar': ")
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()
        break

