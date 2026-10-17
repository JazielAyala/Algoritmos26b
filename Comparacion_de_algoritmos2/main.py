
# ===    COMPARACIÓN DE ALGORITMOS 2     ===
# ===   Diego Antonio Espinosa Salinas   ===
# ===    Brayan Jaziel Navarro Ayala     ===

# ===   FUNCIÓN MAIN   ===
import matplotlib.pyplot as plt
import tkinter as tk
from benchmark import generarListas

def iniciarPrograma():
    inicio = int(entryInicio.get())
    fin = int(entryFin.get())
    incremento = int(entryIncremento.get())

    list1, list2, list3, list4, list5, list6, list7 = generarListas(inicio, fin, incremento)

    # Gráfica
    plt.cla()
    plt.plot(list(list7), list1, marker="o", label="Selection Sort")
    plt.plot(list(list7), list2, marker="o", label="Bubble Sort")
    plt.plot(list(list7), list3, marker="o", label="Insertion Sort")
    plt.plot(list(list7), list4, marker="o", label="Gnome Sort")
    plt.plot(list(list7), list5, marker="o", label="Exchange Sort")
    # plt.plot(list(list7), list6, marker="o", label="Stooge Sort")

    plt.title("Comparación de algoritmos")
    plt.xlabel("Tamaño de entrada n")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.legend()
    plt.grid()
    plt.show()

# ===   VENTANA GUI     ===
#   Ventana, título y tamaño
root = tk.Tk()
root.title("Comparación de Algoritmos")
root.geometry("480x272")

#   Apariencia
root.configure(bg="#121314")

#   Etiquetas y entradas de texto
lblInicio = tk.Label(root, text = "Inicio", fg="#FFFFFF", bg="#121314", font=("Arial", 12))
lblInicio.pack(pady = 10)
entryInicio = tk.Entry(root, fg="#FFFFFF", bg="#1F1F1F", font=("Arial", 12))
entryInicio.pack(pady = 5)

lblIncremento = tk.Label(root, text = "Incremento", fg="#FFFFFF", bg="#121314", font=("Arial", 12))
lblIncremento.pack(pady = 10)
entryIncremento = tk.Entry(root, fg="#FFFFFF", bg="#1F1F1F", font=("Arial", 12))
entryIncremento.pack(pady = 5)

lblFin = tk.Label(root, text = "Fin", fg="#FFFFFF", bg="#121314", font=("Arial", 12))
lblFin.pack(pady = 10)
entryFin = tk.Entry(root, fg="#FFFFFF", bg="#1F1F1F", font=("Arial", 12))
entryFin.pack(pady = 5)

#   Botón
btn = tk.Button(root, text = "Ejecutar programa", command=iniciarPrograma, fg="#FFFFFF", bg="#007ACC", activeforeground="#FFFFFF", activebackground="#005999", relief="flat", bd=0, cursor="hand2", width=15, height=2)
btn.pack(pady = 10)

#   Loop constante
root.mainloop()