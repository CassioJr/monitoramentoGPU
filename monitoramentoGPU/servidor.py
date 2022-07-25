import socket
import GPUtil
from _thread import *

class Servidor:
    
    # Metódo que inicializa as variaveis com o valor passado
    # @param ip Endereço de ip do servidor
    # @param porta Porta destinada ao servidor
    def __init__(self, ip, porta):
        self.ip = ip
        self.porta = porta

    # Metodo que realiza a incialização do servidor 
    def inicializar(self):
        
        # Metódo que cria um socket para a conexão
        # @Param AF_INET IPV4
        # @Param SOCK_STREAM Significa que é um protocolo TCP 
        self.servidor_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor_Socket.bind((self.ip, self.porta))
        print('Servidor foi inicializado!')
        self.servidor_Socket.listen(5)

        # Método utilizado para pegar as GPUs disponiveis no computador
        # return retorna a primeira GPU do array
        def pegar_InfoGPU():
            GPUs = GPUtil.getGPUs()
            gpu = GPUs[0]
            return gpu
       
        # Método que realiza a conexão com o cliente, onde são enviadas as informações de operações que podem ser realizadas
        # Onde tambem é tratado da questao de multiplos clientes conectados
        def cliente_thread(serv):
            print(f"Conexão realizada com o cliente: {endereco[0]}:{endereco[1]}")
            serv.sendall(bytes("\nDigite um número para receber os dados referentes a GPU: \n1- Para monitorar todos os dados \n2- Para monitorar o total de memória da GPU \n3- Para monitorar a memória livre e utilizada da GPU \n4- Para monitorar o consumo em '%' da GPU", "utf-8"))

            while True:
                data = serv.recv(1024)
                # Estrutura de decisão para informar se um cliente foi desconectado
                if not data:
                    print(f"O cliente {endereco[0]}:{endereco[1]} foi desconectado")
                    serv.close()
                    break
                op = data.decode()
                
                # Estrutura de decisões das mensagens que o servidor pode mandar para o cliente
                # Retorna para o cliente o nome, total de memória, memória livre e utilizada e o total de uso da GPU
                if op == "1":
                    serv.sendall(bytes(f"\nNome da GPU: {pegar_InfoGPU().name}\n Total de Memória: {pegar_InfoGPU().memoryTotal}\n Memória livre: {pegar_InfoGPU().memoryFree}\n Memória utilizada: {pegar_InfoGPU().memoryUsed}\n Total de uso da GPU: {pegar_InfoGPU().memoryUtil:.2f} %", "utf-8"))
                # Retorna para o cliente o total de memória da GPU
                elif op == "2":
                    serv.sendall(bytes(f"Total de Memória: {pegar_InfoGPU().memoryTotal}", "utf-8"))
                # Retorna para o cliente o espaço de memória livre e utilizada da GPU
                elif op == "3":
                    serv.sendall(bytes(f"Memória livre: {pegar_InfoGPU().memoryFree}\n Memória utilizada: {pegar_InfoGPU().memoryUsed}", "utf-8"))
                # Retorna para o cliente a porcentagem de uso da GPU
                elif op == "4":
                    serv.sendall(bytes(f"Total de uso da GPU: {pegar_InfoGPU().memoryUtil:.2f} %", "utf-8"))
                # Retorna a mensagem que a operação é inválida caso o cliente mande qualquer outra coisa
                # Que esteja fora dos opções válidas do menu 
                else:
                    serv.sendall(bytes(f"Operação Inválida!", "utf-8"))

        while True:
            # Aceita a conexão 
            conn, endereco = self.servidor_Socket.accept()
            start_new_thread(cliente_thread, (conn, ))

serv = Servidor('127.0.0.1', 2222)
serv.inicializar()