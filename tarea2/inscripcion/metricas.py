import json
import csv

global tiempo_inicio_list
tiempo_inicio_list = []

global avg_record_size_list
avg_record_size_list = []

metricas = {
    "latencia" : [],
    "throughput" : []
}


def leer_csv() -> list:
    with open('tiempos_finales.csv', mode='r') as file:
        reader = csv.reader(file)
        return [float(row[0]) for row in reader]


def escribir_json():
    tiempo_fin_list = leer_csv()
    
    print(tiempo_inicio_list)
    print(tiempo_fin_list)
    print(avg_record_size_list)
    
    for i in range(len(tiempo_inicio_list)):
        latencia_seg = tiempo_fin_list[i] - tiempo_inicio_list[i] # Latencia en segundos
        latencia_ms = latencia_seg * 1000               # Latencia en milisegundos
        metricas["latencia"].append(latencia_ms)
        
        throughput = avg_record_size_list[i] / latencia_seg  # Throughput en Bps (bytes por segundo)
        metricas["throughput"].append(throughput)
    
    with open('metricas.json', 'w') as archivo:
        json.dump(metricas, archivo, indent = 4)