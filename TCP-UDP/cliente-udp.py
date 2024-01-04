import socket

# Configurações do cliente
HOST = '127.0.0.1'
PORT = 12345

# Criação do socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Loop para enviar e receber dados
while True:
    # Envia dados para o servidor
    message = input("Digite a mensagem a ser enviada para o servidor: ")
    client_socket.sendto(message.encode('utf-8'), (HOST, PORT))

    # Recebe dados do servidor
    data, server_address = client_socket.recvfrom(1024)
    print(f"Recebido do servidor {server_address}: {data.decode('utf-8')}")

# Encerra o socket
client_socket.close()