# Usa una imagen base de Python
FROM python:3.10.12

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el código fuente al contenedor
COPY client.py /app

# Instala las dependencias del proyecto
RUN pip install --upgrade pip
RUN pip install requests