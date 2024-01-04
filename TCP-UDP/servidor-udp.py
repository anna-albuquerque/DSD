import socket

# Configurações do servidor
HOST = '127.0.0.1'
PORT = 12345

# Criação do socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"Servidor aguardando mensagens em {HOST}:{PORT}")

# Loop para receber e enviar dados
while True:
    # Recebe dados do cliente
    data, client_address = server_socket.recvfrom(1024)
    
    if not data:
        break  # Se não houver mais dados, encerra o loop
    
    print(f"Recebido do cliente {client_address}: {data.decode('utf-8')}")

    # Envia dados de volta para o cliente
    message = input("Digite a mensagem a ser enviada para o cliente: ")
    server_socket.sendto(message.encode('utf-8'), client_address)

# Encerra o socket
server_socket.close()