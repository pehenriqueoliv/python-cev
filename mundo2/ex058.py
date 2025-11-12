import random

computador = random.randint(0, 10)
jogador = int(input("Pensei em um numero entre 0 a 10, tenta advinhar: "))

while jogador != computador:
    if computador > jogador:
        jogador = int(input("Mais... Tente novamente: "))
    elif computador < jogador:
        jogador = int(input("Menos... Tente novamente: "))

if computador == jogador:
    print(f"O computador escolheu {computador}, voce ganhou!")
