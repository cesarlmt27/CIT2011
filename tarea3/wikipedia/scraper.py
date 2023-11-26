import os
import wikipedia
import sqlite3

# Crear las carpetas
os.makedirs('carpeta1', exist_ok=True)
os.makedirs('carpeta2', exist_ok=True)

# Crear una conexión a la base de datos
con = sqlite3.connect('../database.db')
cur = con.cursor()

# Crear la tabla documento si no existe
cur.execute('''
    CREATE TABLE IF NOT EXISTS documento(
        documento INTEGER PRIMARY KEY,
        url TEXT
    )
''')

for i in range(30):
    while True:
        try:
            # Obtener una página aleatoria
            page = wikipedia.page(wikipedia.random(pages=1))
            break
        except (wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.PageError):
            continue

    # Obtener el texto de la página
    text = page.content

    # Determinar la carpeta de destino
    if i < 15:
        folder = 'carpeta1'
    else:
        folder = 'carpeta2'

    # Crear el nombre del archivo
    filename = os.path.join(folder, f'documento_{i+1}.txt')
    
    # Guardar el texto en el archivo
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
    
    # Insertar la URL de la página y el número del documento en la tabla documento
    cur.execute('''
        INSERT INTO documento(documento, url)
        VALUES (?, ?)
    ''', (i+1, page.url))

# Hacer commit de la transacción y cerrar la conexión
con.commit()
con.close()