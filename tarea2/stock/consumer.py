from aiokafka import AIOKafkaConsumer
import json
import sqlite3
import asyncio
import correo as c
import time
import csv

con = sqlite3.connect("../database/database.db")
cur = con.cursor()


def escribir_csv(valor: float):
    with open('tiempos_finales.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([valor])


def solicitud_reposicion(timestamp, usuario, agua, huesillo, azucar, mote, canela):
    cur.execute("SELECT id, nombre, correo FROM Maestro WHERE usuario = ?", (usuario,))
    res = cur.fetchone()
    id_number = res[0]
    nombre = res[1]
    correo = res[2]
    
    params = (timestamp, id_number, agua, huesillo, azucar, mote, canela)
    cur.execute("INSERT INTO Reposicion VALUES (?, ?, ?, ?, ?, ?, ?)", params)
    con.commit()
    
    c.enviar_correo(nombre, correo)
    
    tiempo_fin = time.time() # Registrar el tiempo de fin    
    escribir_csv(tiempo_fin)


async def paid():
    consumer = AIOKafkaConsumer(
        "stock", bootstrap_servers='kafka:9092',
        value_deserializer=lambda m: json.loads(m.decode('ascii'))
    )
    await consumer.start()
    async for msg in consumer:
        solicitud_reposicion(msg.timestamp, msg.value['usuario'], msg.value['agua'], msg.value['huesillo'], msg.value['azucar'], msg.value['mote'], msg.value['canela'])


async def main():
    task = asyncio.create_task(paid())
    
    await task


asyncio.run(main())