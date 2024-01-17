class Celular():
    def __init__(self, marca, modelo, camara) :
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    def llamar(self):
        print(f"Estás realizado un llamado desde un: {self.modelo}")
        
    def cortar(self):
        print(f"Haz cortado la llamada desde tu: {self.modelo}")
    
celular1 = Celular("Samsong", "S23", "48MP")
celular2 = Celular("Apple", "Iphone 15 Pro", "96MP")

print(celular1.marca)
#Si llamas al método con print, mientras, el método utiliza igualmente print, este devuelve un None 
print(celular2.cortar())
celular2.llamar()
celular2.cortar()