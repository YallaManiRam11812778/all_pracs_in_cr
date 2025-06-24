# ram_server.py
import socketio
import eventlet
import time
# create a Socket.IO server instance
# data={}
sio = socketio.Server(logger=True, engineio_logger=True)

@sio.on('connect')
def handle_connection(sid, environ):
    print('Client connected')
    # send a message to the client with the 'my_message' event
    sio.emit('my_message', {"data": "Hello, client!"}, room=sid)
    print("*"*50)
    time.sleep(3) 

@sio.on('message')
def message_emitting(sid, data):
    print(f'received data is: {data}')  
    # sio.emit('message',data=data ,room=sid)
    sio2.emit('message', data=data)


   
sio2=socketio.Client()

@sio2.on('connect')
def handle_connect():
	print("server changes as client and connected to sumanth")


# @sio.on('*')
# def reply_from_sumanth(data):
#      print(f"reply_from_sumanth: {data}")

@sio.on('disconnect')
def disconnecty(sid, data):
    print("received from client is: ", data['exiting'])
    print("@"*50,sid)
    sio2.send(data)
    # else:
    #     print("No data received from client.")
    #     sio2.send("No data received from client.")
        # print("received from client is: ",data['exiting'])
        # print(f'disconnected by client with sid_id: {sid}')
        # sio2.send(data['exiting'])
    print('Connected to server as client')
    # time.sleep(2)
    # sio2.disconnect()


sio2.connect('http://0.0.0.0:9090', wait_timeout = 10)

sio2.emit('reply')


# run the Socket.IO server
if __name__ == '__main__':
    app = socketio.WSGIApp(sio)
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 8000)), app)
    