class Album:
    def __init__(self):
        self.fotos = [] 

    def agregar_foto(self, foto):
        self.fotos.append(foto)
        print(f"Foto '{foto}' agregada al álbum.")

    def eliminar_foto(self, foto):
        if foto in self.fotos:
            self.fotos.remove(foto)
            print(f"Foto '{foto}' eliminada del álbum.")
        else:
            print(f"Foto '{foto}' no encontrada.")

    def mostrar_fotos(self):
        if self.fotos:
            print("Fotos en el álbum:", ", ".join(self.fotos))
        else:
            print("El álbum está vacío.")


album = Album()
album.agregar_foto("foto1.jpg")
album.agregar_foto("foto2.jpg")
album.mostrar_fotos()
album.eliminar_foto("foto1.jpg")
album.mostrar_fotos()
