class Termostatos:
    def __init__(self, temperatura):
        self.temperatura = temperatura

    def aumentar_temperatura(self, grados):
        self.temperatura += grados
        print(f"Temperatura aumentada a {self.temperatura}°C.")

    def disminuir_temperatura(self, grados):
        self.temperatura -= grados
        print(f"Temperatura disminuida a {self.temperatura}°C.")

    def mostrar_temperatura(self):
        print(f"La temperatura actual es {self.temperatura}°C.")


termostato = Termostatos(20)  


termostato.mostrar_temperatura()

termostato.aumentar_temperatura(5)

termostato.disminuir_temperatura(3)

termostato.mostrar_temperatura()
