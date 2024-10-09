class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.estado = "durmiendo"
    
    def levantar(self):
        self.estado = "despierto"
    
    def dormir(self):
        self.estado = "durmiendo"
    
    def mostrar(self):
        print(f"{self.nombre} tiene {self.edad} años y está {self.estado}")


persona = Persona("Pepe", 28)
persona.mostrar()
persona .levantar()
persona.mostrar()