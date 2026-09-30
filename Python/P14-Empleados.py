class Empleado:
    def __init__(self,nombre:str, salario_base:float):
        self.nombre = nombre
        self.salario_base = salario_base

class EmpleadoTiempoCompleto(Empleado):
    def calcularSalario(self):
        return self.salario_base

class EmpleadoPorHoras(Empleado):
    def calcularSalario(self,horas:float):
        return self.salario_base*horas

misEmpleados = [
    EmpleadoTiempoCompleto("Jorge", 8000),
    EmpleadoPorHoras("Javier", 1000)
]

print(misEmpleados[0].calcularSalario())
print(misEmpleados[1].calcularSalario(8))
