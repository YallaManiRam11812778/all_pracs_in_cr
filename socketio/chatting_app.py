import threading
import socket
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
ip_address = get_ip_address()

# choice = input("Do you want to host (1) or to connect (2): ")

# if choice == "1":
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip_address, 1231))  # Server binds to this IP and port
server.listen()
client, _ = server.accept()
# elif choice == "2":
#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client.connect((ip_address, 1231))  # Client connects to server's IP and port
# else:
#     exit()

def sending_messages(c):
    while True:
        message = input("")
        c.send(message.encode())

def receiving_messages(c):
    while True:
        try:
            message = c.recv(1024).decode()
            if not message:
                print("Connection closed by server.")
                break
            print("User: " + message)
        except (ConnectionAbortedError, ConnectionResetError):
            print("Connection lost. Exiting receiving messages.")
            break

threading.Thread(target=sending_messages, args=(client,)).start()
threading.Thread(target=receiving_messages, args=(client,)).start()
