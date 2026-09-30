class Libro:
    def __init__(self, titulo:str, autor:str, ISBN:int, disponible:bool = True):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.disponible = disponible
    
    def print(self):
        print("---")
        print(self.titulo)
        print(f"- {self.autor} -")
        print(self.ISBN)
        print("DISPONIBLE" if self.disponible else "NO DISPONIBLE")

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro:Libro):
        self.libros.append(libro)

    def buscar(self, titulo:str):
        for libro in self.libros:
            if titulo.lower() in libro.titulo.lower():
                libro.print()

    def tomar(self, libro:Libro):
        libro.disponible = False

mibib = Biblioteca()

PJ1 = Libro("Percy Jackson y los dioses del olimpo I: el ladron del rayo", "Rick R. Riordan", 123123123)
PJ2 = Libro("Percy Jackson y los dioses del olimpo II: el mar de monstruos", "Rick R. Riordan", 123123124)
mibib.agregar_libro(PJ1)
mibib.agregar_libro(PJ2)
mibib.buscar("Percy")

