from kafka import KafkaProducer # !pip install kafka-python !pip list | grep kafka
import json, time, random

producer = KafkaProducer(
    bootstrap_servers='ec-kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = {
        "tipoEvento": "orden.creada",
        "ordenId": random.randint(1, 1000),
        "total": random.randint(50, 1500),
        "estado": "PENDIENTE",
        "origen": "python",
        "timestamp": int(time.time())
    }

    producer.send("orden-eventos", value=data)
    print("Enviado:", data)

    time.sleep(2)