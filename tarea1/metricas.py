import matplotlib.pyplot as plt
import numpy as np
import json

limite = 10000  # Límite de valores a graficar

def plot_line_chart(x, y1, y2, title, xlabel, ylabel):
    plt.plot(x, y1, label="Caché casero", marker='o')
    plt.plot(x, y2, label="Memcached", marker='o')
    
    intervalos_x = np.arange(0, limite+1, limite/10)
    etiquetas_x = [str(x) for x in intervalos_x]
    plt.xticks(intervalos_x, etiquetas_x)
    
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.show()


with open('./cache_casero/cache server/app/search/metricas_casero.json', 'r') as archivo:
    metricas_casero = json.load(archivo)
    
    numero_busqueda = [clave for clave in metricas_casero["tiempo_busqueda"].keys()]
    tiempo_casero = [valor for valor in metricas_casero["tiempo_busqueda"].values()]

with open('./memcached/search/metricas_memcached.json', 'r') as archivo:
    metricas_memcache = json.load(archivo)

    tiempo_memcached = [valor for valor in metricas_memcache["tiempo_busqueda"].values()]


numero_busqueda = numero_busqueda[:limite]
tiempo_casero = tiempo_casero[:limite]
tiempo_memcached = tiempo_memcached[:limite]

plot_line_chart(numero_busqueda, tiempo_casero, tiempo_memcached, "Tiempo de búsquedas sucesivas", "Número de búsqueda", "Tiempo (segundos)")