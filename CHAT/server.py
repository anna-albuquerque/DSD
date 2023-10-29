import Pyro4

@Pyro4.expose
class TextServer(object):
    def __init__(self):
        self.text = ""

    def send_text(self, text):
        self.text = text
        return "Texto atualizado com sucesso."

    def get_text(self):
        return self.text

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()

uri = daemon.register(TextServer)
ns.register("text.server", uri)

print("Aguardando conexões...")
daemon.requestLoop()