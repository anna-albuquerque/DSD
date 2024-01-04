import socket

# Configurações do servidor
HOST = '127.0.0.1'
PORT = 12345

# Criação do socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Servidor aguardando conexão em {HOST}:{PORT}")

# Aceitação de conexões
client_socket, client_address = server_socket.accept()
print(f"Conexão recebida de {client_address}")

# Loop para receber e enviar dados
while True:
    # Recebe dados do cliente
    data = client_socket.recv(1024)
    
    if not data:
        break  # Se não houver mais dados, encerra o loop
    
    print(f"Recebido do cliente: {data.decode('utf-8')}")

    # Envia dados de volta para o cliente
    message = input("Digite a mensagem a ser enviada para o cliente: ")
    client_socket.sendall(message.encode('utf-8'))

# Encerra a conexão
client_socket.close()
server_socket.close()