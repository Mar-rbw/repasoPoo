class A:
    def hablar(self):
        print("Hola desde A")

class B:
    def hablar(self):
        print("Hola desde B")
       
class C:
    def hablar(self):
        print("Hola desde C")

class E(A):
    def hablar(self):
        print("Hola desde E")

class F(B):
    def hablar(self):
        print("Hola desde F")
        
class G(C):
    def hablar(self):
        print("Hola desde G")

class H(E, F):
    def hablar(self):
        print("Hola desde H")

class I(F, G):
    def hablar(self):
        print("Hola desde I")

class Z:
    def hablar(self):
        print("Hola desde Z")

class J(H, Z, I):
    def hablar(self):
        print("Hola desde J")

class K(J):
    def hablar(self):
        print("Hola desde K")

d = K()

d.hablar()

#Para saber el recorrido de las herencias aplicadas a alguna clase se ocupa el siguiente comando
print(K.mro())

Z.hablar(d)