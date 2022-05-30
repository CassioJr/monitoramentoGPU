import socket
from monitoramentoGPU import Monitor

HOST = "127.0.0.1"
PORT= 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    a= Monitor;
    servidor.bind((HOST, PORT))
    servidor.listen()
    while True:
        serv, adress = servidor.accept()
        print(f"Conexão realizada: {adress[0]}:{adress[1]}")
        serv.sendall(bytes(a.getGPUStats(), "utf-8"))