import random
class Alumnos:
    def __init__(self, nombre:str, matricula:int):
        self.nombre = nombre
        self.matricula = matricula
        self.calificaciones = []

    def new_cali(self, calificacion:float):
        self.calificaciones.append(calificacion)
    
    def promedio(self):
        prom = 0
        for i, cali in enumerate(self.calificaciones):
            prom = ((prom * i) + cali) / (i + 1)
        return prom
    
    def esta_aprobado(self):
        return self.promedio() >= 6

misAlumnos = [
    Alumnos("Alicia"   , 74185963),
    Alumnos("Batista"  , 74561230),
    Alumnos("Charlie"  , 78941230),
    Alumnos("Daniela"  , 78461230),
    Alumnos("Elizabeth", 78945123)
]

for alumno in misAlumnos:
    alumno.new_cali(random.randint(50,100)/10)
    alumno.new_cali(random.randint(50,100)/10)
    alumno.new_cali(random.randint(50,100)/10)
    print(f"{alumno.nombre} tiene {alumno.promedio()}")

mejores = []
mejor_cali = 0
for alumno in misAlumnos:
    if alumno.promedio() > mejor_cali:
        mejor_cali = alumno.promedio()
        mejores.clear()
        mejores.append(alumno)
    elif alumno.promedio() == mejor_cali:
        mejores.append(alumno)

print("Mejor(es):")
for alumno in mejores:
    print(alumno.nombre)
