from Mamifero import Mamifero
from Ave import Ave

class Murcielago(Mamifero, Ave):
    pass
    
murcielago = Murcielago()

murcielago.comer()
murcielago.amamantar()
murcielago.volar()

print(Murcielago.mro())