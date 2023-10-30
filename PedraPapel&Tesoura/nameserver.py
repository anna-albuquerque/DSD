import Pyro4

# Inicialize o Name Server
Pyro4.config.SERVERTYPE = "multiplex"

with Pyro4.Daemon(host="localhost", port=9090) as daemon:
    ns = Pyro4.locateNS()
    daemon.register(ns, "Pyro.NameServer")
    daemon.requestLoop()
