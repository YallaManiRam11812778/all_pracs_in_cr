# lkshmn_client.py

import socketio
import sys
import time
# create a Socket.IO client instance
sio = socketio.Client()

# define a function to handle the 'connect' event
@sio.on('connect')
def handle_connect():
    print('Connected to server')

@sio.on('my_message')
def handle_my_message(data):
    time.sleep(5)
    print("111111111111111111111111")
    print('Received message:', data['data'])
    message=input("give some data for sending to client: ")
    sio.emit("message",message)
    
    
@sio.on('received')
def received_from_ram(data):    
    sio.emit('message',data=data)
    print("222222222222222222222222")
    
# @sio.on('message')
# def msg():


# connect to the Socket.IO server
sio.connect('http://0.0.0.0:8000', wait_timeout = 10)

# sio.wait()
time.sleep(10)
disconnected=input("want to disconnect?: ")
if disconnected=='yes':
    # try:
        # @sio.on('disconnect')
        # def disconnect(sid):
        sio.emit('disconnect',{'exiting':'disconnect 555555555555555 by user client'})
        print(f"disconnected by client")
        sio.disconnect()
    # finally:
    #     sys.exit()


# message = {'ob': 'house',
#            'ids': ['54fjadb70f9756','39f1ax451f6567']}

# print(message)

# wait for events
