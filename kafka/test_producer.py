from kafka import KafkaProducer
from json import dumps
from time import sleep


producer = KafkaProducer(bootstrap_servers=['172.17.0.1:9093'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

for e in range(10):
    print('sending')
    data = {'1': e}
    producer.send('productViewCount', value=data)
    sleep(1)
