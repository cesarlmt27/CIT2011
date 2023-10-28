from kafka import KafkaProducer
from kafka.errors import KafkaError
import json

producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                         value_serializer=lambda m: json.dumps(m).encode('ascii'))

def formulario(data, partition):
    producer.send('inscripcion', value=data, partition=partition)