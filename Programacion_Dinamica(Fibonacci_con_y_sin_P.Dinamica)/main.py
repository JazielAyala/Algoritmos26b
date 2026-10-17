import matplotlib.pyplot as plt
import tkinter as tk
from benchmark import generarValor

def iniciarPrograma():
    inicio = int(entryInicio.get())
    fin = int(entryFin.get())
    incremento = int(entryIncremento.get())

    t_bruta, t_dinamica, tamanhos = generarValor(inicio, fin, incremento)

    # Gráfica
    plt.cla()
    plt.plot(tamanhos, t_bruta, marker="o", label="Fuerza Bruta")
    plt.plot(tamanhos, t_dinamica, marker="o", label="Programación Dinámica")
    plt.yscale("log")
    plt.title("Comparación de Complejidad: Fibonacci")
    plt.xlabel("Tamaño de entrada n")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)
    plt.show()

# === VENTANA GUI ===
root = tk.Tk()
root.title("Comparación de Algoritmos - Fibonacci")
root.geometry("480x300")
root.configure(bg="#121314")

lblInicio = tk.Label(root, text="Inicio", fg="#FFFFFF", bg="#121314", font=("Arial", 11))
lblInicio.pack(pady=5)
entryInicio = tk.Entry(root, fg="#FFFFFF", bg="#1F1F1F", font=("Arial", 11), justify="center")
entryInicio.pack(pady=2)

lblIncremento = tk.Label(root, text="Incremento", fg="#FFFFFF", bg="#121314", font=("Arial", 11))
lblIncremento.pack(pady=5)
entryIncremento = tk.Entry(root, fg="#FFFFFF", bg="#1F1F1F", font=("Arial", 11), justify="center")
entryIncremento.pack(pady=2)

lblFin = tk.Label(root, text="Fin", fg="#FFFFFF", bg="#121314", font=("Arial", 11))
lblFin.pack(pady=5)
entryFin = tk.Entry(root, fg="#FFFFFF", bg="#1F1F1F", font=("Arial", 11), justify="center")
entryFin.pack(pady=2)

btn = tk.Button(
    root, 
    text="Ejecutar prueba", 
    command=iniciarPrograma, 
    fg="#FFFFFF", 
    bg="#007ACC", 
    activeforeground="#FFFFFF", 
    activebackground="#005999", 
    relief="flat", 
    bd=0, 
    cursor="hand2", 
    width=18, 
    height=2
)
btn.pack(pady=15)

root.mainloop()