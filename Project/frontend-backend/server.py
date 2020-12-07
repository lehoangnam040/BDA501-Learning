from flask import Flask, request
from flask_cors import CORS, cross_origin
from kafka import KafkaProducer
from json import dumps

app = Flask(__name__)
cors = CORS(app)
producer = KafkaProducer(bootstrap_servers=['localhost:9093'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

@app.route("/view/<product_id>", methods=['GET', 'POST'])
def test(product_id):
    print(product_id)
    # Ban len kafka
    data = {'product': str(product_id)}
    producer.send('productView', value=data)
    return 'OK'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
