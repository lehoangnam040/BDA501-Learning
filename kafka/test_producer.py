from kafka import KafkaProducer
from json import dumps
from time import sleep


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

for e in range(10):
    data = {'number' : e}
    producer.send('sample', value=data)
    sleep(5)
