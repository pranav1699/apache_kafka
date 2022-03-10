import json
from kafka import KafkaConsumer
from numpy import source


if __name__ == "__main__":
    consumer = KafkaConsumer(
        'fromdb',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest'
    )
    for message in consumer:
        data = message.value
        
        print(data)
