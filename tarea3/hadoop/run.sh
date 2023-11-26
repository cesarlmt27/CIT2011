#!/bin/bash

echo -e "\nEjecutando script de Hadoop"

# Creación de carpeta para usuario
hdfs dfs -mkdir /user

# Creación de usuario en el directorio
hdfs dfs -mkdir /user/hduser

# Creación de directorio para el procesamiento archivos y/o textos
hdfs dfs -mkdir input

# Permisos tantos del usuario y del directorio
sudo chown -R hduser .

# Cargar archivos a HDFS
hdfs dfs -put wikipedia/carpeta1/*.txt input
hdfs dfs -put wikipedia/carpeta2/*.txt input

# Ejecutar `mapper.py` y `reducer.py` para cada archivo
mapred streaming -files mapper.py,reducer.py -input /user/hduser/input/*.txt -output hduser/outhadoop/ -mapper ./mapper.py -reducer ./reducer.py

# Descargar archivos de HDFS
hdfs dfs -get /user/hduser/hduser/outhadoop/ /home/hduser/wikipedia/