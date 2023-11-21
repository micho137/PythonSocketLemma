from flask import Flask, jsonify
from flask_socketio import SocketIO, emit
from red import preprocess_text
import os

app = Flask(__name__)

api_cors_config = {
    "origins":["http://localhost:4890"],
    "methods":["OPTIONS", "GET", "POST"],
    "allow_headers":["Authorization", "Content-Type"]
}

socket_io = SocketIO(app, resource={
    r"/*": api_cors_config
})

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

@app.route('/')
def ping():
    return jsonify({"response":"Desplegado correctamente"})

if __name__ == '__main__':
    port = os.getenv('PORT')

    if port is None:
        port = 4890

    app.run(host="0.0.0.0", port=port, debug=True)