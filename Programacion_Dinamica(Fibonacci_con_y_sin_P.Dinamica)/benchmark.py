
import time
import fibonacciBruta
import FibonacciDinamica

def medir_tiempos_bruta(lista, limite=35):
    tiempos = []
    for n in lista:
        if n <= limite:
            t_ini = time.time()
            fibonacciBruta.fibonacci(n)
            t_fin = time.time()
            tiempos.append(t_fin - t_ini)
        else:
            tiempos.append(None)  
    return tiempos

def medir_tiempos_dinamica(lista):
    tiempos = []
    for n in lista:
        t_ini = time.time()
        FibonacciDinamica.fibonacci_dp(n)
        t_fin = time.time()
        tiempos.append(t_fin - t_ini)
    return tiempos

def generarValor(inicio, fin, incremento):
    listaTamanhos = list(range(inicio, fin + 1, incremento))
    
    t_bruta = medir_tiempos_bruta(listaTamanhos, limite=35)
    t_dinamica = medir_tiempos_dinamica(listaTamanhos)
    
    return t_bruta, t_dinamica, listaTamanhos