from tabulate import tabulate
from colorama import init, Fore, Style

class Tarea:
    def __init__(self, descripcion, completada=False):
        self.descripcion = descripcion
        self.completada = completada

    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        estado = "completada" if self.completada else "pendiente"
        return f"Tarea: {self.descripcion} - Estado: {estado}"

class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas pendientes.")
        else:
            print(Fore.MAGENTA + "\n--- Lista de tareas ---" + Fore.WHITE)
            headers = ["#", "Descripción", "Estado"]
            table = []
            for i, tarea in enumerate(self.tareas, start=1):
                estado = "Completada" if tarea.completada else "Pendiente"
                table.append([i, tarea.descripcion, estado])
            print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

    def marcar_completada(self, indice):
        try:
            tarea = self.tareas[indice - 1]
            tarea.marcar_completada()
            print(f"Tarea '{tarea.descripcion}' marcada como completada.")
        except IndexError:
            print("La posición especificada no existe en la lista de tareas.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

    def eliminar_tarea(self, indice):
        try:
            tarea = self.tareas.pop(indice - 1)
            print(Fore.GREEN + f"Tarea '{tarea.descripcion}' eliminada.")
        except IndexError:
            print(Fore.RED + "La posición especificada no existe en la lista de tareas.")
        except Exception as e:
            print(Fore.RED + f"Ocurrió un error: {e}")

if __name__ == "__main__":
    lista = ListaTareas()

    while True:
        print(Fore.MAGENTA + "\n--- Menú ---")
        menu = [
            [Fore.YELLOW + "1", "Agregar una nueva tarea"],
            [Fore.GREEN +  "2", "Marcar una tarea como completada"],
            [Fore.BLUE +   "3", "Mostrar todas las tareas"],
            [Fore.MAGENTA +"4", "Eliminar una tarea"],
            [Fore.RED +    "5", "Salir"]
        ]
        print(Fore.WHITE + tabulate(menu, headers=["Opción", "Descripción"], tablefmt="fancy_grid"))
        print(Style.RESET_ALL)

        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción de la nueva tarea: ")
            lista.agregar_tarea(descripcion)
        elif opcion == "2":
            lista.mostrar_tareas()
            indice = int(input("Ingrese el número de la tarea que desea marcar como completada: "))
            lista.marcar_completada(indice)
        elif opcion == "3":
            lista.mostrar_tareas()
        elif opcion == "4":
            lista.mostrar_tareas()
            indice = int(input("Ingrese el número de la tarea que desea eliminar: "))
            lista.eliminar_tarea(indice)
        elif opcion == "5":
            print(Fore.RED + "¡Hasta luego!")
            break
        else:
            print(Fore.RED + "Opción no válida. Por favor, ingrese un número válido.")
