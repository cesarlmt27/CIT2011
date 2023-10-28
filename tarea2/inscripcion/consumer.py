from kafka import KafkaConsumer
from kafka.structs import TopicPartition
import json
import sqlite3

def add_db(nombre, usuario, correo, paid):
    params = (nombre, usuario, correo, paid)
    cur.execute("INSERT INTO Usuario VALUES (?, ?, ?, ?)", params)
    con.commit()
    

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('inscripcion',
                         bootstrap_servers=['kafka:9092'],
                         group_id='aprobacion',
                         value_deserializer=lambda m: json.loads(m.decode('ascii')))

con = sqlite3.connect("../database/database.db")
cur = con.cursor()

for msg in consumer:
    if msg.partition == 1:
        print('Paid')
        add_db(msg.value['nombre'], msg.value['usuario'], msg.value['correo'], msg.value['paid'])
    elif msg.partition == 0:
        print('Normal')
        add_db(msg.value['nombre'], msg.value['usuario'], msg.value['correo'], msg.value['paid'])
    else:
        print('Partición no esperada.')