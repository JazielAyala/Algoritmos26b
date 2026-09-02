import matplotlib.pyplot as plt 
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random 
import time 

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort_brute_force(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def iniciar_grafica():
    inicio = int(caja_inicio.get())
    aumento = int(caja_aumento.get())
    maximo = int(caja_maximo.get())

    n_valores = []
    tiempos_selection = []
    tiempos_bubble = []

    boton_graficar.config(text="Calculando... (Puede tardar)")
    
    for actual_n in range(inicio, maximo + 1, aumento):

        arr_base = [random.randint(0, 1000) for _ in range(actual_n)]
        arr_sel = arr_base.copy()
        arr_bub = arr_base.copy()

        t0 = time.time()
        selection_sort(arr_sel)
        tiempo_sel = time.time() - t0


        t0 = time.time()
        bubble_sort_brute_force(arr_bub)
        tiempo_bub = time.time() - t0


        n_valores.append(actual_n)
        tiempos_selection.append(tiempo_sel)
        tiempos_bubble.append(tiempo_bub)

        ventana.update()


    ax.clear()
    
    ax.plot(n_valores, tiempos_selection, marker="o", label="Selection Sort")
    ax.plot(n_valores, tiempos_bubble, marker="o", label="Bubble Sort")
    
    ax.set_title("Comparación de algoritmos")
    ax.set_xlabel("Tamaño de entrada n")
    ax.set_ylabel("Tiempo de ejecución (s)")
    ax.legend()
    ax.grid(True)
    
    canvas.draw()
    

    boton_graficar.config(text="Graficar Resultados")


ventana = tk.Tk()
ventana.title("Comparador de Algoritmos")
ventana.geometry("700x600")

frame_controles = tk.Frame(ventana)
frame_controles.pack(pady=10)


tk.Label(frame_controles, text="Iniciar en:").grid(row=0, column=0, padx=5)
caja_inicio = tk.Entry(frame_controles, width=10)
caja_inicio.insert(0, "20")
caja_inicio.grid(row=0, column=1, padx=5)

tk.Label(frame_controles, text="Aumentar en:").grid(row=0, column=2, padx=5)
caja_aumento = tk.Entry(frame_controles, width=10)
caja_aumento.insert(0, "20") 
caja_aumento.grid(row=0, column=3, padx=5)

tk.Label(frame_controles, text="Fin:").grid(row=0, column=4, padx=5)
caja_maximo = tk.Entry(frame_controles, width=10)
caja_maximo.insert(0, "400") 
caja_maximo.grid(row=0, column=5, padx=5)


boton_graficar = tk.Button(ventana, text="Graficar Resultados", command=iniciar_grafica, bg="lightblue")
boton_graficar.pack(pady=5)

figura, ax = plt.subplots(figsize=(6, 4))
canvas = FigureCanvasTkAgg(figura, master=ventana)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

ventana.mainloop()