import socket

# Informações sobre o IP e a porta do servidor
HOST = "127.0.0.1"
PORT= 2222

# Metódo que cria um socket para a conexão
# @Param AF_INET IPV4
# @Param SOCK_STREAM Significa que é um protocolo TCP 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    # Realiza a conexão com as informações passadas do servidor
    servidor.connect((HOST,PORT))
    #Recebe as informações do servidor de quais ações poderá realizar
    buffer = servidor.recv(1024)
    buffer = buffer.decode("utf-8")
    print(f"{buffer}")
    op = input()

    # Estrutura de decisão das mensagens que podem ser enviadas ao servidor
    match op:
        case '1':
            servidor.sendall((bytes(op, "utf-8")))
            data = servidor.recv(1024)
            print(data.decode())
        case '2':
            servidor.sendall((bytes(op, "utf-8")))
            data = servidor.recv(1024)
            print(data.decode())
        case '3':
            servidor.sendall((bytes(op, "utf-8")))
            data = servidor.recv(1024)
            print(data.decode())
        case '4':
            servidor.sendall((bytes(op, "utf-8")))
            data = servidor.recv(1024)
            print(data.decode())
        case default:
            servidor.sendall((bytes(op, "utf-8")))
            data = servidor.recv(1024)
            print(data.decode())