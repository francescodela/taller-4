class Bibliotecas:
    def __init__(self):
        self.libros = []  

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro}' agregado a la biblioteca.")

    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print(f"Libro '{libro}' eliminado de la biblioteca.")
        else:
            print(f"Libro '{libro}' no encontrado.")

    def mostrar_libros(self):
        if self.libros:
            print("Libros en la biblioteca:", ", ".join(self.libros))
        else:
            print("La biblioteca está vacía.")


biblioteca = Bibliotecas()

biblioteca.agregar_libro("Cien años de soledad")
biblioteca.agregar_libro("Don Quijote de la Mancha")
biblioteca.mostrar_libros()
biblioteca.eliminar_libro("Cien años de soledad")
biblioteca.mostrar_libros()

