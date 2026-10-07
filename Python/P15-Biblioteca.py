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

    def mostrar(self):
        for libro in self.libros:
            libro.print()

    def buscar(self, titulo:str):
        for libro in self.libros:
            if titulo.lower() in libro.titulo.lower():
                libro.print()

    def tomar(self, libro:Libro):
        libro.disponible = False
        if libro in self.libros:
            self.libros.remove(libro)
        else:
            print("Libro no disponible")

    def devolver(self, libro:Libro):
        libro.disponible = True
        self.libros.append(libro)

mibib = Biblioteca()

PJ1 = Libro("Percy Jackson y los dioses del olimpo I: el ladron del rayo", "Rick R. Riordan", 123123123)
PJ2 = Libro("Percy Jackson y los dioses del olimpo II: el mar de monstruos", "Rick R. Riordan", 123123124)
PHM = Libro(
    "Project Hail Mary",
    "Andy weir",
    789789789
)
print(f"\nPRUEBA: agregar 3 libros")
mibib.agregar_libro(PJ1)
mibib.agregar_libro(PJ2)
mibib.agregar_libro(PHM)
print(f"\nPRUEBA: Mostrar libreria")
mibib.mostrar()
print(f"\nPRUEBA: Busqueda (Percy)")
mibib.buscar("Percy")
print(f"\nPRUEBA: Tomar")
mibib.tomar(PJ1)
mibib.mostrar()
print(f"\nPRUEBA: Tomar ya tomado")
mibib.tomar(PJ1)
print(f"\nPRUEBA: Devolver")
mibib.devolver(PJ1)

mibib.mostrar()
