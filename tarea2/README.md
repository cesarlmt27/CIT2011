# Comandos de Kafka

## Creación de topic con dos particiones
```bash
kafka-topics.sh --create --bootstrap-server kafka:9092 --topic inscripcion --partitions 2
```

## Detalles de un topic
```bash
kafka-topics.sh --describe --bootstrap-server kafka:9092 --topic my_topic
```

## Listar todos los topics
```bash
kafka-topics.sh --list --bootstrap-server kafka:9092
```

## Consumidor desde consola (para ver contenido)
```bash
kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic my_topic --partition 0 --from-beginning
```



# Comandos varios

## Iniciar un servidor local SMTP de depuración con Python
```bash
python -m smtpd -c DebuggingServer -n cliente:1025
```