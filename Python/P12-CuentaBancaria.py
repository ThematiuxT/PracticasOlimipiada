class CuentaBancaria:
    def __init__(self, titular:str, saldo:float, numero_cuenta:int):
        self.titular = titular
        self.saldo = saldo
        self.numero_cuenta = numero_cuenta

    def depositar(self, cantidad:float):
        if cantidad < 0:
            print("No se puede depositar una cantidad negativa")
            return
        self.saldo = self.saldo + cantidad 

    def retirar(self, cantidad:float):
        if cantidad < 0:
            print("No se puede retirar una cantidad negativa")
            return
        if cantidad > self.saldo:
            print("No se puede retirar mas de la cantidad en la cuenta")
            return
        self.saldo = self.saldo - cantidad

    def consulta(self):
        print(self.titular, self.numero_cuenta)
        print(f"{self.saldo}$")

mi_cuenta = CuentaBancaria(
    "Mateo",
    500,
    120240613
)

mi_cuenta.consulta()
mi_cuenta.retirar(501)
mi_cuenta.retirar(-1)
mi_cuenta.depositar(-1)
mi_cuenta.depositar(1)
mi_cuenta.consulta()
mi_cuenta.retirar(1)
mi_cuenta.consulta()

