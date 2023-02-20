from procesos.secuencialmente import secuencial
from procesos.multiprocesamiento import multiproceso
from time import time

def main():
    sec = time()
    print("Ejecucion secuencial: ", '\n')
    secuencial()
    print("El tiempo de ejecucion mediante la forma secuencial es: ", time() - sec, "segundos", '\n')
    mult = time()
    print("Ejecucion multiproceso: ", '\n')
    multiproceso()
    print("El tiempo de ejecucion mediante multiprocesamiento es: ", time() - mult, "segundos")