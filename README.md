# 1a_paralelo

Link del repositorio: [Github](https://github.com/GonzaloGmv/1a_paralelo)

En esta tarea tenemos que ejecutar un código secuencialmente y con multiproceso y así podemos comprobar cual es más eficaz para este caso.

El código que se ejecutará es el siguiente:
```
import random
from time import sleep

def scrape(url):
    print("starting", url)
    duration = round(random.random(), 3)
    sleep(duration)
    print("finished", url, "time taken:", duration, "seconds")
    return url, duration
```
### Secuencial
```
from scrape import scrape

urls = ["a.com", "b.com", "c.com", "d.com"]

def secuencial():
    output = []
    for url in urls:
        result = scrape(url)
        output.append(result)
    print('\n')
    for i in output:
        print(i)
```
### Multiproceso
```
from multiprocessing import Pool
from scrape import scrape

urls = ["a.com", "b.com", "c.com", "d.com"]

def multiproceso():
    pool = Pool(processes=4)
    data = pool.map(scrape, urls)
    pool.close()    
    print()
    for row in data:
        print(row)
```
### Lanzador
Para ver lo que tarda en ejecutarse cada proceso utilizamos la funcion time(). Esto lo hemos ejecutado en el lanzador:
```
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
```
### Main
Y finalmete lo ejecutamos todo desde el main
```
from lanzador import main

if __name__ == '__main__':
    main()
```
### Conclusión
Esta es una captura de pantalla de la terminal con todo el código ejecutado. Aquí podemos ver que es más eficaz el multiproceso. Esto es debido a que la secuencial va una por una, mientras que el multiproceso hace las cuatro a la vez.

![image](https://user-images.githubusercontent.com/91721237/220144742-3f7fbca4-8697-40d8-b3cb-fdf4717a8c14.png)
