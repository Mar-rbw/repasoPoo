class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
        
    def obtener_datos(self):
        return f"Datos del estudiante:\n\tNombre:{self.nombre}\n\tEdad:{self.edad}"
