# sumanth_server.py
import socketio
import eventlet
import time
# create a Socket.IO server instance
sio = socketio.Server(logger=True, engineio_logger=True)

# define a function to handle the 'connect' event
@sio.on('connect')
def handle_connect(sid, environ):
    print('server_1 connected _________________')
    # send a message to the client with the 'my_message' event
    sio.emit('my_message', {"data": "Hello, client!"}, room=sid)
    print("*"*50)
    time.sleep(3)
    sio.emit('message')
# @sio.on('message')
# def message(sid,data):
        # sio.emit('message', data=data,room=sid)
# #         print("000000000000000000000000000000000")


# @sio.on('*')
# def replying_to_client(sid, data):
#     sio.emit('*', {'data': 'foobar'}, room=sid)
#     print("$$$$$$$$$$$$$$$$$$$$$$$$$    from custom event     $$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#     data=input("wt would u say to lksmn client: ")
#     sio.emit('reply', data=data, room=sid)
#     print(f"replying_to_client lkshmn with sid_id: {sid} and data is: {data}")



# @sio.on('reply')
# def replying_to_client(sid, data):
#     print("$$$$$$$$$$$$$$$$$$$$$$$$    from reply      $$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#     data=input("wt would u say to lksmn client: ")
#     sio.emit('reply', data=data, room=sid)
#     print(f"replying_to_client lkshmn with sid_id: {sid} and data is: {data}")


    
@sio.on('disconnect')
def disconnect(sid):   
    # sio.emit('disconnect',data['exiting'])
    print("."*100)
    # print(f"received data is: {data}")
    # print("received from client is: ",data['exiting'])
    print(f'disconnected by client with sid_id: {sid}')


# run the Socket.IO server
if __name__ == '__main__':
    app = socketio.WSGIApp(sio)
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 9090)), app)
    