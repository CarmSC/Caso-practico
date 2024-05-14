import tkinter as tk
from tkinter import messagebox

class TareasPendientes:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append({"descripcion": tarea, "completada": False})

    def marcar_completada(self, indice):
        try:
            self.tareas[indice]["completada"] = True
        except IndexError:
            mostrar_error("La posición ingresada no existe en la lista de tareas.")

    def mostrar_tareas(self):
        if not self.tareas:
            return "No hay tareas pendientes."
        else:
            tareas = ""
            for i, tarea in enumerate(self.tareas):
                estado = "Completada" if tarea["completada"] else "Pendiente"
                tareas += f"{i+1}. {tarea['descripcion']} - {estado}\n"
            return tareas

    def eliminar_tarea(self, indice):
        try:
            del self.tareas[indice]
        except IndexError:
            mostrar_error("La posición ingresada no existe en la lista de tareas.")


def mostrar_error(mensaje):
    ventana_error = tk.Toplevel()
    ventana_error.title("Error")
    tk.Label(ventana_error, text=mensaje, padx=20, pady=20).pack()
    boton_cerrar = tk.Button(ventana_error, text="Cerrar", command=ventana_error.destroy)
    boton_cerrar.pack()

def agregar_tarea():
    tarea = entrada_tarea.get()
    lista_tareas.agregar_tarea(tarea)
    entrada_tarea.delete(0, tk.END)  # Limpiar el texto del Entry después de agregar la tarea
    actualizar_texto()

def marcar_completada():
    indice = int(entrada_indice.get()) - 1
    lista_tareas.marcar_completada(indice)
    entrada_indice.delete(0, tk.END) 
    actualizar_texto()

def mostrar_tareas():
    texto_tareas.config(state="normal")
    texto_tareas.delete(1.0, tk.END)
    texto_tareas.insert(tk.END, lista_tareas.mostrar_tareas())
    texto_tareas.config(state="disabled")

def eliminar_tarea():
    try:
        indice = entrada_indice_eliminar.get()
        if indice.isdigit():  # Verificar si el índice es un número
            indice = int(indice) - 1
            if 0 <= indice < len(lista_tareas.tareas):  # Verificar si el índice está dentro del rango válido
                lista_tareas.eliminar_tarea(indice)
                entrada_indice_eliminar.delete(0, tk.END)
                actualizar_texto()
            else:
                mostrar_error("La posición ingresada no existe en la lista de tareas.")
        else:
            mostrar_error("Ingrese un número válido para el índice.")
        
    except ValueError:
        mostrar_error("Ingrese un número válido para el índice.")
    except IndexError:
        mostrar_error("La posición ingresada no existe en la lista de tareas.")

def actualizar_texto():
    mostrar_tareas()

# Crear ventana
ventana = tk.Tk()
ventana.title("Gestión de Tareas")

# Definir dimensiones de la ventana
ventana.geometry("650x650")  # Ancho x Alto

# Crear frame para contener el formulario
frame_formulario = tk.Frame(ventana)
frame_formulario.grid(pady=80)

# Ajustar tamaño del frame después de crearlo
frame_formulario.config(width=400, height=200)

# Crear instancia de la clase TareasPendientes
lista_tareas = TareasPendientes()

# Crear entrada para agregar tarea
tk.Label(frame_formulario, text="Agregar Tarea:").grid(row=0, column=0)
entrada_tarea = tk.Entry(frame_formulario)
entrada_tarea.grid(row=0, column=1)
boton_agregar = tk.Button(frame_formulario, text="Agregar", command=agregar_tarea)
boton_agregar.grid(row=0, column=2)

# Crear entrada para marcar tarea como completada
tk.Label(frame_formulario, text="Marcar como Completada (índice):").grid(row=1, column=0)
entrada_indice = tk.Entry(frame_formulario)
entrada_indice.grid(row=1, column=1)
boton_completada = tk.Button(frame_formulario, text="Completada", command=marcar_completada)
boton_completada.grid(row=1, column=2)

# Crear entrada para eliminar tarea
tk.Label(frame_formulario, text="Eliminar Tarea (índice):").grid(row=2, column=0)
entrada_indice_eliminar = tk.Entry(frame_formulario)
entrada_indice_eliminar.grid(row=2, column=1)
boton_eliminar = tk.Button(frame_formulario, text="Eliminar", command=eliminar_tarea)
boton_eliminar.grid(row=2, column=2)

# Crear botón para mostrar todas las tareas
boton_mostrar_tareas = tk.Button(frame_formulario, text="Mostrar Tareas", command=mostrar_tareas, 
                                 relief=tk.RAISED, bg="#007BFF", fg="white", 
                                 font=("Arial", 8, "bold"), padx=10, pady=5,
                                 borderwidth=2, highlightthickness=0, 
                                 bd=3, activebackground="#55a055", activeforeground="white")
boton_mostrar_tareas.grid(row=10, column=0, columnspan=3, pady=10)  # Añadir pady para crear un espacio

# Crear texto para mostrar las tareas
texto_tareas = tk.Text(frame_formulario, height=10, width=50)
texto_tareas.grid(row=12, column=1, columnspan=3, pady=10)
texto_tareas.config(state="disabled")

# Iniciar bucle de eventos
ventana.mainloop()
