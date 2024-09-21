class Animal:
    def __init__(self, nombre, tipo, edad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Edad: {self.edad} años"

class NodoAnimal:
    def __init__(self, animal=None):
        self.animal = animal
        self.siguiente = None

class ListaEnlazadaAnimales:
    def __init__(self):
        self.cabeza = None

    def agregar_animal(self, animal):
        if self.buscar_animal(animal.nombre):
            print(f"El animal {animal.nombre} ya está en la lista.")
            return
        
        nuevo_nodo = NodoAnimal(animal)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        print(f"Animal {animal.nombre} agregado exitosamente.")

    def mostrar_animales(self):
        if not self.cabeza:
            print("La lista está vacía.")
            return

        actual = self.cabeza
        while actual:
            print(actual.animal)
            actual = actual.siguiente

    def buscar_animal(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.animal.nombre == nombre:
                return actual.animal
            actual = actual.siguiente
        return None

    def mostrar_animal_por_nombre(self, nombre):
        animal = self.buscar_animal(nombre)
        if animal:
            print(f"Animal encontrado: {animal}")
        else:
            print(f"No se encontró un animal con el nombre {nombre}")

if __name__ == '__main__':
    lista_animales = ListaEnlazadaAnimales()

    while True:
        print("\nMenú:")
        print("1. Agregar un nuevo animal")
        print("2. Mostrar todos los animales")
        print("3. Buscar un animal por nombre")
        print("4. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            nombre = input("Ingrese el nombre del animal: ")
            tipo = input("Ingrese el tipo de animal (Águila, Pantera, Vaca, etc.): ")
            edad = int(input("Ingrese la edad del animal: "))
            animal = Animal(nombre, tipo, edad)
            lista_animales.agregar_animal(animal)

        elif opcion == 2:
            lista_animales.mostrar_animales()

        elif opcion == 3:
            nombre = input("Ingrese el nombre del animal que desea buscar: ")
            lista_animales.mostrar_animal_por_nombre(nombre)

        elif opcion == 4:
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")
