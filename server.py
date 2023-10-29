import Pyro4
import random

# Definindo a classe do jogo de Pedra, Papel e Tesoura
class RPSGame(object):
    def __init__(self):
        self.choices = ["pedra", "papel", "tesoura"]

    def play(self, player_choice):
        server_choice = random.choice(self.choices)
        if player_choice not in self.choices:
            return "Escolha inválida. Escolha entre pedra, papel ou tesoura."
        if player_choice == server_choice:
            return f"Empate! Ambos escolheram {player_choice}."
        if (player_choice == "pedra" and server_choice == "tesoura") or \
           (player_choice == "papel" and server_choice == "pedra") or \
           (player_choice == "tesoura" and server_choice == "papel"):
            return f"Você ganhou! Você escolheu {player_choice}, e o servidor escolheu {server_choice}."
        else:
            return f"Você perdeu! Você escolheu {player_choice}, e o servidor escolheu {server_choice}."

# Inicializando o servidor Pyro
daemon = Pyro4.Daemon()
uri = daemon.register(RPSGame)

print("Aguardando conexões...")
daemon.requestLoop()