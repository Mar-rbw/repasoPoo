def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la función")
        funcion()
        print("Despues de llamar a la función")
    return funcion_modificada

def saludar():
    print("Hola como andas")
    
saludo_modificado = decorador(saludar)
saludo_modificado()

#Son lo mismo pero más modulado
def saludo():
    print("Hola como andas, la venganza")
    
saludo()