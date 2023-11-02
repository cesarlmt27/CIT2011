from kafka import KafkaProducer
import json
import metricas as m

producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                         value_serializer=lambda m: json.dumps(m).encode('ascii'))

def venta(data):
    producer.send('venta', value=data)
    
    metricas = producer.metrics()   # Diccionario anidado con las métricas
    avg_record_size = metricas['producer-metrics']['record-size-avg']   # Tamaño promedio de un registro
    m.avg_record_size_list.append(avg_record_size)