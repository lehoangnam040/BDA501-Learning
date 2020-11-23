from kafka import KafkaProducer
from json import dumps
from time import sleep


producer = KafkaProducer(bootstrap_servers=['192.168.1.24:9093'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

for e in range(10):
    print('sending')
    data = {'text': 'le hoang nam ' + str(e)}
    producer.send('wordcount', value=data)
    sleep(1)
