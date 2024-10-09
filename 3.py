class Libros:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible.")

    def devolver(self):
        self.disponible = True
        print(f"El libro '{self.titulo}' ha sido devuelto.")

    def mostrarestado(self):
        estado = "disponible" if self.disponible else "prestado"
        print(f"El libro '{self.titulo}' está {estado}.")


libro1 = Libros("Cien años de soledad", "Gabriel García Márquez")
libro1.mostrarestado()
libro1.prestar()
libro1.mostrarestado()
libro1.devolver()

libro1.mostrarestado()
