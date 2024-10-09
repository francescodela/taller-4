class Temporizador:
    def __init__(self, tiempo_inicial):
        self.tiempo_restante = tiempo_inicial  

    def iniciar(self):
        print(f"Temporizador iniciado con {self.tiempo_restante} segundos.")

    def pausar(self):
        print(f"Temporizador pausado con {self.tiempo_restante} segundos restantes.")

    def mostrar(self):
        print(f"Tiempo restante: {self.tiempo_restante} segundos.")


temporizador = Temporizador(170)  
temporizador.iniciar()
temporizador.pausar()
temporizador.mostrar()
