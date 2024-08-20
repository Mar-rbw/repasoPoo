class Auto():
    def __init__(self) -> None:
        self.__estado = "apagado"
        
    def encender(self):
        self.__estado = "encendido"
        print("El auto está encendido")
        
    def conducir(self):
        if self.__estado == "apagado":
            self.encender()
        print("Conduciendo el auto")
        
mi_auto = Auto()
mi_auto.conducir()