import socket

HOST = "127.0.0.1"
PORT= 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST,PORT))
buffer = server.recv(1024)
buffer = buffer.decode("utf-8")
print(f"{buffer}")