class CarritoDeCompras:
    def __init__(self):
        self.productos = [] 

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto '{producto}' fue agregado al carrito.")

    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
            print(f"Producto '{producto}' fue  eliminado del carrito.")
        else:
            print(f"El producto '{producto}' no está en el carrito.")

    def mostrar_productos(self):
        if self.productos:
            print("Productos en el carrito:", ", ".join(self.productos))
        else:
            print("El carrito está vacío.")


carrito = CarritoDeCompras()
carrito.agregar_producto("yuca")
carrito.agregar_producto("platano")
carrito.mostrar_productos()
carrito.eliminar_producto("platano")
carrito.mostrar_productos()
