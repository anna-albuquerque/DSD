import Pyro4

# Inicialize o Name Server
Pyro4.config.SERVERTYPE = "multiplex"
Pyro4.naming.NameServerDaemon.serveSimple(
    host="localhost", port=9090, enableBroadcast=True)
