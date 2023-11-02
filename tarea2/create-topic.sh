#!/bin/bash

# Ejecución de los archivos del "ENTRYPOINT" y del "CMD" especificados en el Dockerfile de Bitnami,
# y espera de 10 segundos para que esté en ejecución el servidor de Apache Kafka
/opt/bitnami/scripts/kafka/entrypoint.sh /opt/bitnami/scripts/kafka/run.sh & sleep 10

# Creación de topic "inscripcion" con dos particiones
kafka-topics.sh --create --bootstrap-server kafka:9092 --topic inscripcion --partitions 2

# Creación de topic "stock"
kafka-topics.sh --create --bootstrap-server kafka:9092 --topic stock

# Creación de topic "venta"
kafka-topics.sh --create --bootstrap-server kafka:9092 --topic venta

# Mantener el contenedor en ejecución
tail -f /dev/null