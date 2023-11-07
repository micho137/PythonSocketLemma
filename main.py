from flask import Flask
from flask_socketio import SocketIO, emit
from red import preprocess_text
import os

app = Flask(__name__)

app.debug = True

app.config['SECRET_KEY'] = 'secret!'

socket_io = SocketIO(app, cors_allowed_origins="*")

@socket_io.on('connect')
def test_connect():
    print('Cliente Conectado')

@socket_io.on('disconnect')
def test_disconnect():
    print('Cliente disconnectado')

@socket_io.on('TextOutput')
def handleText(data):
    GLOSA = []
    processed_text = preprocess_text(data)
    GLOSA.append(processed_text)
    print(GLOSA)
    emit('ProcessedText', GLOSA)

if __name__ == '__main__':
    socket_io.run(app, host="0.0.0.0", port=5000)

