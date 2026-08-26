import tkinter as tk

def saludar():
    nombre = entrada.get().strip()
    if not nombre:
        nombre = "Jaziel"
    lbl.config(text=f"Hola Compa, {nombre}")
root = tk.Tk()
root.title("Saludador de Compas")
root.geometry("360x220")
#Crear etiqueta
lbl = tk.Label(root, text = "Hola, Escribe tu nombre y presiona el boton")
lbl.pack(pady = 10)
#Entrada de texto
entrada = tk.Entry(root)
entrada.pack(pady = 10)

#Creacion de boton
btn = tk.Button(root, text="Saludar", command=saludar)
btn.pack(pady=10)
root.mainloop()