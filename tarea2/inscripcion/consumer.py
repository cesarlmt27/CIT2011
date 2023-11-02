from aiokafka import AIOKafkaConsumer
import json
import sqlite3
import asyncio
import correo as c
import random
import string
import time
import csv

con = sqlite3.connect("../database/database.db")
cur = con.cursor()


def escribir_csv(valor: float):
    with open('tiempos_finales.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([valor])


def inscripcion(nombre, usuario, correo, paid, clave):
    params = (nombre, usuario, correo, paid, clave)
    cur.execute("INSERT INTO Maestro (nombre, usuario, correo, paid, clave) VALUES (?, ?, ?, ?, ?)", params)
    con.commit()
    
    cur.execute("SELECT * FROM Maestro WHERE id = ?", (cur.lastrowid,))
    res = cur.fetchone()
    
    c.enviar_correo(res[1], res[2], res[3], res[5])
    
    tiempo_fin = time.time() # Registrar el tiempo de fin    
    escribir_csv(tiempo_fin)


def generar_pass():
    # get random string of letters and digits
    source = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(source) for i in range(12)))
    return result_str


# Process 1
async def paid():
    consumer = AIOKafkaConsumer(
        "inscripcion", bootstrap_servers='kafka:9092',
        group_id="aprobacion",
        value_deserializer=lambda m: json.loads(m.decode('ascii'))
    )
    await consumer.start()
    async for msg in consumer:
        print('Paid')
        clave = generar_pass()
        inscripcion(msg.value['nombre'], msg.value['usuario'], msg.value['correo'], msg.value['paid'], clave)


# Process 2
async def normal():
    consumer2 = AIOKafkaConsumer(
        "inscripcion", bootstrap_servers='kafka:9092',
        group_id="aprobacion",
        value_deserializer=lambda m: json.loads(m.decode('ascii'))
    )
    await consumer2.start()
    async for msg in consumer2:
        print('Normal')
        clave = generar_pass()
        inscripcion(msg.value['nombre'], msg.value['usuario'], msg.value['correo'], msg.value['paid'], clave)
        await asyncio.sleep(1)
        
        
async def main():
    task = asyncio.create_task(paid())
    task2 = asyncio.create_task(normal())
    
    await task
    await task2


asyncio.run(main())