# server/server.py
from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

clients = set()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    clients.add(request.sid)
    print(f'Client connected: {request.sid}')
    emit('message', 'A new user has joined the chat.', broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    clients.remove(request.sid)
    print(f'Client disconnected: {request.sid}')
    emit('message', 'A user has left the chat.', broadcast=True)

@socketio.on('message')
def handle_message(msg):
    print(f'Message: {msg}')
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True, debug = True)

