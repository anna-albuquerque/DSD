import Pyro4

# Conectando ao servidor Pyro
with Pyro4.Proxy("PYRONAME:text.server") as text_server:
    while True:
        text = input("Digite o texto para enviar (ou 'sair' para encerrar): ")
        if text == 'sair':
            break
        response = text_server.send_text(text)
        print(response)