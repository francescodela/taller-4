class ListaTareas:
    def __init__(self):
        self.tareas = [] 

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        print(f"Tarea '{tarea}' agregada a la lista.")

    def eliminar_tarea(self, tarea):
        if tarea in self.tareas:
            self.tareas.remove(tarea)
            print(f"Tarea '{tarea}' eliminada de la lista.")
        else:
            print(f"Tarea '{tarea}' no encontrada.")

    def mostrar_tareas(self):
        if self.tareas:
            print("Tareas pendientes:", ", ".join(self.tareas))
        else:
            print("No hay tareas pendientes.")


lista = ListaTareas()
lista.agregar_tarea("estudiar  para  el parcial ")
lista.agregar_tarea("hacer el taller ")
lista.mostrar_tareas()




