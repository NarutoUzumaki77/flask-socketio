from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = "sush7e9whwdbs89wiebshbs7e9i9wensbsd7w8"
socketio = SocketIO(app)

msg = []
DEFAULT = {'data': 'User Connected'}


@app.route('/')
def sessions():
    return render_template('session.html')


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    append_to_msg(json)
    print(msg)
    socketio.emit('my response', msg, callback=messageReceived)


def append_to_msg(notification):
    if notification != DEFAULT:
        msg.append(notification)


if __name__ == '__main__':
    socketio.run(app, debug=True)
