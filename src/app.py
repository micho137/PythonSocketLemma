from flask import Flask, jsonify
from flask_socketio import SocketIO, emit
from red import preprocess_text
import os

app = Flask(__name__)

socket_io = SocketIO(app, cors_allowed_origins="https://prototalk.onrender.com/")

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

@app.route('/', methods=['GET'])
def ping():
    return jsonify({"response":"Hola, esto sirve"})

if __name__ == '__main__':
    port = os.getenv('PORT')

    if port is None:
        port = 4890

    app.run(host="0.0.0.0", port=port, debug=True)