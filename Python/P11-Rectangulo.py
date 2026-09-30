class Rectangulo:
    def __init__(self,base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base*self.altura

    def perimetro(self):
        return 2*self.base + 2*self.altura
    
    def es_cuadrado(self):
        return self.base == self.altura

rect = Rectangulo(5,7)
print(f"Rectangulo de {rect.base} por {rect.altura}")
print(f"tiene un area de {rect.area()}\ny un perimetro de {rect.perimetro()}")
if rect.es_cuadrado():
    print("es un cuadrado")
else:
    print("no es un cuadrado")
