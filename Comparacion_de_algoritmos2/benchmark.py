import random
import time
from ordenamientos import selection_sort, bubble_sort_brute_force, insertion_sort, gnome_sort, stooge_sort_rec, exchange_sort

# ===  GENERADOR DE NÚMEROS ALEATORIOS  ===
def generarAleatorios(n, min, max):
    '''
    n   → Cantidad de números aleatorios
    min → Valor mínimo de los números aleatorios
    max → Valor máximo de los números aleatorios 
    '''
    temp = []
    for i in range(n):
        temp.append(random.randint(min, max))
    return (temp)

# ===  FUNCIONES DE ORDENAMIENTO  ===
def ordenar(funcion, lista):
    tiempos = []
    for i in lista:
        t_ini = time.time()
        funcion(i)
        t_fin = time.time()
        tiempos.append(t_fin - t_ini)
    return tiempos

def ordenarStooge(lista):
    tiempos = []
    for i in lista:
        t_ini = time.time()
        stooge_sort_rec(i, 0, len(i) - 1)
        t_fin = time.time()
        tiempos.append(t_fin - t_ini)
    return tiempos

# ===  GENERADOR DE LISTAS Y PRUEBA DE FUNCIONAMIENTO  ===
def generarListas(inicio, fin, incremento):
    listas_n1 = []
    listas_n2 = []
    listas_n3 = []
    listas_n4 = []
    listas_n5 = []
    listas_n6 = []
    listaTamanhos = []

    for i in range(inicio, fin + 1, incremento):
        listas_n1.append(generarAleatorios(i, 1, 100))
        listas_n2.append(generarAleatorios(i, 1, 100))
        listas_n3.append(generarAleatorios(i, 1, 100))
        listas_n4.append(generarAleatorios(i, 1, 100))
        listas_n5.append(generarAleatorios(i, 1, 100))
        listas_n6.append(generarAleatorios(i, 1, 100))
        listaTamanhos.append(i)

    t_selection = []
    t_bubble = []
    t_insertion = []
    t_gnome = []
    t_stooge = []
    t_exchange = []

    t_selection = ordenar(selection_sort, listas_n1)
    t_bubble = ordenar(bubble_sort_brute_force, listas_n2)
    t_insertion = ordenar(insertion_sort, listas_n3)
    t_gnome = ordenar(gnome_sort, listas_n4)
    t_stooge = ordenarStooge(listas_n5)
    t_exchange = ordenar(exchange_sort, listas_n6)

    return t_selection, t_bubble, t_insertion, t_gnome, t_exchange, t_stooge, listaTamanhos