import Pyro4

# Conectando ao servidor Pyro
uri = "PYRONAME:rps_game"
rps_game = Pyro4.Proxy(uri)

# Loop do cliente
while True:
    player_choice = input("Escolha pedra, papel ou tesoura (ou 'sair' para encerrar): ")
    if player_choice == 'sair':
        break
    result = rps_game.play(player_choice)
    print(result)
