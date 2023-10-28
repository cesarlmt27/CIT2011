# Comandos de Kafka

## Creación de topic `inscripcion` con dos particiones
```bash
kafka-topics.sh --create --bootstrap-server kafka:9092 --topic inscripcion --partitions 2
```

## Detalles del topic
```bash
kafka-topics.sh --describe --bootstrap-server kafka:9092 --topic inscripcion
```

## Listar todos los topics
```bash
kafka-topics.sh --list --bootstrap-server kafka:9092
```

## Consumidor desde consola (para ver contenido)
```bash
kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic inscripcion --partition 0 --from-beginning
```