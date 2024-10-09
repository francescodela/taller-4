class CuentaDeBanco:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def deposita(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente")

    def mostrar(self):
        print(f"El saldo de {self.titular} es {self.saldo}.")

# Ejemplo de uso
cuenta = CuentaDeBanco("Frank", 4999)
cuenta.mostrar()

# Depósito
cuenta.deposita(500)
cuenta.mostrar()

# Retiro
cuenta.retirar(1000)
cuenta.mostrar()

# Intento de retirar más de lo que hay
cuenta.retirar(10000)
