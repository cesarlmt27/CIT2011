import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Maestro(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre, usuario, correo, paid, clave)")

cur.execute("CREATE TABLE IF NOT EXISTS Reposicion(timestamp PRIMARY KEY, usuario_id, agua, huesillo, azucar, mote, canela)")

cur.execute("CREATE TABLE IF NOT EXISTS Venta(timestamp PRIMARY KEY, maestro_id, monto)")

con.commit()
con.close()