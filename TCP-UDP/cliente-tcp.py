import socket

# Configurações do cliente
HOST = '127.0.0.1'
PORT = 12345

# Criação do socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Loop para enviar e receber dados
while True:
    # Envia dados para o servidor
    message = input("Digite a mensagem a ser enviada para o servidor: ")
    client_socket.sendall(message.encode('utf-8'))

    # Recebe dados do servidor
    data = client_socket.recv(1024)
    print(f"Recebido do servidor: {data.decode('utf-8')}")

# Encerra a conexão
client_socket.close()