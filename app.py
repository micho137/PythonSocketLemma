from flask import Flask, jsonify
from flask_socketio import SocketIO, emit
from red import preprocess_text
import os

app = Flask(__name__)
socket_io = SocketIO(app, cors_allowed_origins="*")

@socket_io.on('connect')
def handle_connect():
    print('Cliente Conectado')

@socket_io.on('disconnect')
def handle_disconnect():
    print('Cliente desconectado')

@socket_io.on('TextOutput')
def handle_text(data):
    GLOSA = []
    processed_text = preprocess_text(data)
    GLOSA.append(processed_text)
    print(GLOSA)
    emit('ProcessedText', GLOSA, broadcast=True)

@app.route('/')
def ping():
    return jsonify({"response": "Desplegado correctamente"})

if __name__ == '__main__':

    socket_io.run(app, host="0.0.0.0", debug=False, use_reloader=False)
