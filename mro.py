class A:
    def hablar(self):
        print("Hola desde A")
        
class B:
    def hablar(self):
        print("Hola desde B")

class F(B):
    pass
        
class C(A, F):
    pass
        
class E(C, F):
    pass
        
class D(E):
    pass
        
d = D()

d.hablar()