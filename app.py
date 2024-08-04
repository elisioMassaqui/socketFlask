from flask import Flask, render_template
from flask_socketio import SocketIO, send
import subprocess

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index_ws.html')
@socketio.on('message')
def handle_message(message, a=3, b=5):
    a = 15
    b = 15
    x = a + b
    #y = subprocess.run('arduino-cli version', capture_output=True)
    print('Received message:', message)
    send(f'Hello from Flask!, Valor: a + b = : {x}')

if __name__ == '__main__':
    socketio.run(app, debug=True)
