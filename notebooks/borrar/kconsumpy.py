from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "orden-eventos",
    bootstrap_servers='localhost:19092',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Escuchando eventos...")

for i, msg in enumerate(consumer):
    print(msg.value)
    if i >= 4:
        break