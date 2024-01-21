class Gato():
    def sonido(self):
        return "Miau"

class Perro():
    def sonido(self):
        return "Guau"
    
def hacerSonido(animal):
    print(animal.sonido())
    
gato = Gato()
perro = Perro()

hacerSonido(gato)

print(gato.sonido())