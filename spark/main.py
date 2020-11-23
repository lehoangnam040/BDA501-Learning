from flask import Flask, request
import socket
from time import sleep

# Setup spark streaming connection
TCP_IP = "0.0.0.0"
TCP_PORT = 9008
conn = None
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_obj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket_obj.bind((TCP_IP, TCP_PORT))
socket_obj.listen(1)
print("Waiting for TCP connection...")
conn, addr = socket_obj.accept()
print("Connected to spark streaming")

app = Flask(__name__)

def send_to_spark(mess, tcp_connection):
    try:
        tcp_connection.send(bytes(f'{mess}\n', 'utf-8'))
        #sleep(1)
    except Exception as e:
        print(str(e))

@app.route("/test", methods=['GET', 'POST'])
def test():
    req_body = request.get_json()
    mess = req_body.get('message', '')
    send_to_spark(mess, conn)
    return 'OK'

if __name__ == "__main__":
    app.run()
