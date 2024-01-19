#hereda persona , grado, metodo: imprimir grado de estudiante
from Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado) -> None:
        super().__init__(nombre, edad)
        self.grado = grado

    def obtener_grado(self):
        return f"\n\tGrado: {self.grado}"

manuel = Estudiante("Manuel", 17, "3°M")
print(f"{manuel.obtener_datos()}{manuel.obtener_grado()}")

