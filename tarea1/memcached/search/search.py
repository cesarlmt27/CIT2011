import time
import numpy as np
from find_car_by_id import find_car_by_id
from pymemcache.client.base import Client
import json

# Inicializar conexión con Memcached
memcached = Client(('memcached', 11211))

class CacheClient:
    def get(self, key, simulated=False):
        start_time = time.time()  # Inicio del temporizador

        value = memcached.get(key)
        
        if value:
            elapsed_time = time.time() - start_time  # Calcula el tiempo transcurrido
            print(f"Time taken (cache): {elapsed_time:.5f} seconds")
            return value.decode('utf-8')  # Decodifica el valor desde bytes a cadena
        else:
            # Simulamos un retraso aletorio de 1 a 3 segundos, con una distribución normal en 2
            delay = np.random.normal(2, 0.5)
            print(f"Key not found in cache. Waiting {delay:.5f} seconds...")

            if not simulated:
                time.sleep(delay)

            # Si no está en el caché, buscar en el JSON
            value = find_car_by_id(int(key))
            value = str(value)
            if value:
                print("Key found in JSON. Adding to cache...")
                
                # Agregando la llave-valor al caché
                memcached.set(key, value.encode('utf-8'))  # Codifica el valor a bytes
                
                elapsed_time = time.time() - start_time  # Calcula el tiempo transcurrido
                if simulated:
                    # add delay to time just sum
                    elapsed_time += delay
                print(f"Time taken (JSON + delay): {elapsed_time:.5f} seconds")
                
                return value
            else:
                elapsed_time = time.time() - start_time  # Calcula el tiempo transcurrido
                print(f"Time taken: {elapsed_time:.5f} seconds")
                print("Key not found.")
                return None
            
    def simulate_searches(self, n_searches=100):
        keys_to_search = [f"{i}" for i in np.random.randint(1, 101, n_searches)]
        
        tiempo_busqueda = dict()

        # Métricas
        time_without_cache = 0
        time_with_cache = 0
        avoided_json_lookups = 0

        count = 0
        for key in keys_to_search:
            # clear console
            count += 1
            print("\033[H\033[J")
            print(f"Searching : {count}/{n_searches}")
            start_time = time.time()
            time_without_cache += 3 + 0.001  # Estimado de tiempo de búsqueda en JSON
            self.get(key)
            elapsed_time = time.time() - start_time
            time_with_cache += elapsed_time

            if elapsed_time < 1:
                avoided_json_lookups += 1
                
            tiempo_busqueda[count] = elapsed_time

        time_saved = time_without_cache - time_with_cache
        print(f"\nTime saved thanks to cache: {time_saved:.2f} seconds")
        print(f"Number of times JSON lookup was avoided: {avoided_json_lookups}")
        
        metricas = {
            "tiempo_busqueda" : tiempo_busqueda,
            "busquedas_evitadas" : avoided_json_lookups,
            "tiempo_ahorrado" : time_saved
        }
        
        with open('metricas_memcached.json', 'w') as archivo:
            json.dump(metricas, archivo, indent = 4)
        

if __name__ == '__main__':

    client = CacheClient()

    while True:
        print("\nChoose an operation:")
        print("1. Get")
        print("2. Simulate Searches")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            key = input("Enter key: ")
            value = client.get(key)
            if value is not None:
                print(f"Value: {value}")
        elif choice == "2":
            n_searches = int(input("Enter the number of searches you want to simulate: "))
            client.simulate_searches(n_searches)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")