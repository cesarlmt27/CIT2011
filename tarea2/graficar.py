import matplotlib.pyplot as plt
import json

def graficar_json(archivo: str, titulo):
    with open(archivo, 'r') as file:
        data = json.load(file)
        latencia = data['latencia']
        throughput = data['throughput']
        x_latencia = range(1, len(latencia) + 1)
        x_throughput = range(1, len(throughput) + 1)
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
        
        # Gráfica de latencia
        ax1.plot(x_latencia, latencia, label='Latencia')
        ax1.set_xlabel('Número del mensaje')
        ax1.set_ylabel('Latencia (ms)')
        ax1.set_title('Gráfica de latencia')
        ax1.legend()
        
        # Gráfica de throughput
        ax2.plot(x_throughput, throughput, label='Throughput', color='green')
        ax2.set_xlabel('Número del mensaje')
        ax2.set_ylabel('Throughput (Bps)')
        ax2.set_title('Gráfica de throughput')
        ax2.legend()
        
        plt.suptitle(titulo)
        
        plt.tight_layout()
        
        
graficar_json("inscripcion/metricas.json", "Inscripción")

graficar_json("stock/metricas.json", "Gestión de ingredientes")

graficar_json("venta/metricas.json", "Recuento de ventas")

plt.show()