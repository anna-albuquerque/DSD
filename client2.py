import Pyro4

# Conectando ao servidor Pyro
with Pyro4.Proxy("PYRONAME:text.server") as text_server:
    while True:
        remote_text = text_server.get_text()
        print("Texto recebido do servidor: ", remote_text)