import tkinter as tk

def submit():
    print("Nombre:", nombre.get())
    print("Edad:", edad.get())

# Crear ventana
ventana = tk.Tk()
ventana.title("Formulario")

# Crear etiquetas
tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
tk.Label(ventana, text="Edad:").grid(row=1, column=0)

# Crear campos de entrada
nombre = tk.Entry(ventana)
edad = tk.Entry(ventana)

# Colocar campos de entrada en la ventana
nombre.grid(row=0, column=1)
edad.grid(row=1, column=1)

# Crear botón de enviar
tk.Button(ventana, text="Enviar", command=submit).grid(row=2, column=0, columnspan=2)

# Iniciar bucle de eventos
ventana.mainloop()