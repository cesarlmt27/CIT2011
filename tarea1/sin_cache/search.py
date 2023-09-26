import time
import numpy as np
from find_car_by_id import find_car_by_id

class CacheClient:
    def get(self, key, simulated=False):
        start_time = time.time()  # Inicio del temporizador

        # Buscar en el JSON
        value = find_car_by_id(int(key))
        value = str(value)
        if value:
            print("Key found in JSON.")
            
            elapsed_time = time.time() - start_time  # Calcula el tiempo transcurrido
            print(f"Time taken (JSON): {elapsed_time:.5f} seconds")
            
            return value
        else:
            elapsed_time = time.time() - start_time  # Calcula el tiempo transcurrido
            print(f"Time taken: {elapsed_time:.5f} seconds")
            print("Key not found.")
            return None
            
    def simulate_searches(self, n_searches=100):
        keys_to_search = [f"{i}" for i in np.random.randint(1, 101, n_searches)]

        # Métricas
        time_without_cache = 0

        count = 0
        for key in keys_to_search:
            # clear console
            count += 1
            print("\033[H\033[J")
            print(f"Searching : {count}/{n_searches}")
            start_time = time.time()
            time_without_cache += 3 + 0.001  # Estimado de tiempo de búsqueda en JSON
            find_car_by_id(int(key))
            elapsed_time = time.time() - start_time

        print(f"\nTime taken (simulated): {time_without_cache:.2f} seconds")
        print(f"\nTime taken (real): {elapsed_time:.2f} seconds")
        

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