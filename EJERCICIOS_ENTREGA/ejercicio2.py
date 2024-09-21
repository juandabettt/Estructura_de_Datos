from datetime import datetime

class Tarea:
    def __init__(self, descripcion, prioridad, fecha_vencimiento):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%Y-%m-%d")

    def __str__(self):
        return f"Descripción: {self.descripcion}, Prioridad: {self.prioridad}, Fecha de Vencimiento: {self.fecha_vencimiento.strftime('%Y-%m-%d')}"

class NodoTarea:
    def __init__(self, tarea=None):
        self.tarea = tarea
        self.siguiente = None

class ListaEnlazadaTareas:
    def __init__(self):
        self.cabeza = None

    def agregar_tarea(self, tarea):
        nuevo_nodo = NodoTarea(tarea)
        
        
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            
            actual = self.cabeza
            anterior = None

            while actual and (actual.tarea.prioridad < tarea.prioridad or 
                              (actual.tarea.prioridad == tarea.prioridad and actual.tarea.fecha_vencimiento <= tarea.fecha_vencimiento)):
                anterior = actual
                actual = actual.siguiente
            
            if anterior is None:  
                nuevo_nodo.siguiente = self.cabeza
                self.cabeza = nuevo_nodo
            else:  
                nuevo_nodo.siguiente = actual
                anterior.siguiente = nuevo_nodo

        print(f"Tarea '{tarea.descripcion}' agregada exitosamente.")

    def mostrar_tareas(self):
        if not self.cabeza:
            print("La lista de tareas está vacía.")
            return
        
        actual = self.cabeza
        while actual:
            print(actual.tarea)
            actual = actual.siguiente

    def buscar_tarea(self, descripcion):
        actual = self.cabeza
        while actual:
            if actual.tarea.descripcion == descripcion:
                return actual.tarea
            actual = actual.siguiente
        return None

    def eliminar_tarea(self, descripcion=None, posicion=None):
        if not self.cabeza:
            print("La lista de tareas está vacía.")
            return
        
        actual = self.cabeza
        anterior = None
        index = 0

        
        if descripcion:
            while actual and actual.tarea.descripcion != descripcion:
                anterior = actual
                actual = actual.siguiente
            if not actual:
                print(f"No se encontró la tarea con la descripción '{descripcion}'.")
                return

        
        elif posicion is not None:
            while actual and index != posicion:
                anterior = actual
                actual = actual.siguiente
                index += 1
            if not actual:
                print(f"No se encontró la tarea en la posición {posicion}.")
                return
        
        
        if anterior is None:  
            self.cabeza = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente
        
        print(f"Tarea '{actual.tarea.descripcion}' eliminada exitosamente.")

    def marcar_completada(self, descripcion):
        self.eliminar_tarea(descripcion=descripcion)

if __name__ == '__main__':
    lista_tareas = ListaEnlazadaTareas()

    while True:
        print("\nMenú de Gestión de Tareas:")
        print("1. Agregar una tarea")
        print("2. Eliminar una tarea")
        print("3. Mostrar todas las tareas")
        print("4. Buscar una tarea")
        print("5. Marcar una tarea como completada")
        print("6. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            descripcion = input("Ingrese la descripción de la tarea: ")
            prioridad = int(input("Ingrese la prioridad de la tarea (1: alta, 2: media, 3: baja): "))
            fecha_vencimiento = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ")
            tarea = Tarea(descripcion, prioridad, fecha_vencimiento)
            lista_tareas.agregar_tarea(tarea)

        elif opcion == 2:
            print("1. Eliminar por descripción")
            print("2. Eliminar por posición")
            subopcion = int(input("Seleccione una opción: "))
            
            if subopcion == 1:
                descripcion = input("Ingrese la descripción de la tarea a eliminar: ")
                lista_tareas.eliminar_tarea(descripcion=descripcion)
            elif subopcion == 2:
                posicion = int(input("Ingrese la posición de la tarea a eliminar (comienza desde 0): "))
                lista_tareas.eliminar_tarea(posicion=posicion)

        elif opcion == 3:
            lista_tareas.mostrar_tareas()

        elif opcion == 4:
            descripcion = input("Ingrese la descripción de la tarea a buscar: ")
            tarea = lista_tareas.buscar_tarea(descripcion)
            if tarea:
                print(f"Tarea encontrada: {tarea}")
            else:
                print(f"No se encontró una tarea con la descripción '{descripcion}'.")

        elif opcion == 5:
            descripcion = input("Ingrese la descripción de la tarea a marcar como completada: ")
            lista_tareas.marcar_completada(descripcion)

        elif opcion == 6:
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")



