class MiClase:
    def __init__(self, atributoPublico, atributoPrivado, atributoSuperPrivado) -> None:
        self.atributoPublico = atributoPublico
        self._atributoPrivado = atributoPrivado
        self.__atributoSuperPrivado = atributoSuperPrivado
        
    def get_atributo(self):
        return self.__atributoSuperPrivado
    
    def set_atributo(self, atributoSuperPrivado):
        self.__atributoSuperPrivado = atributoSuperPrivado
        
    def hablar(self):
        print("Hola, Como estas?")
        
objeto = MiClase("Esto es un atributo publico", "Esto es un atributo Privado", "Esto es un atributo Super Privado")
print(objeto.get_atributo())

objeto.set_atributo("Esto es un cambio")
print(objeto.get_atributo())