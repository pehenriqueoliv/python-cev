import random 

print("Suas opcoes:")
print("[0] Pedra")
print("[1] Papel")
print("[2] Tesoura")
jogador = int(input("Qual sua opcao?: "))

computador = random.randint(0, 2)

if jogador == 0 and computador == 1:
    print("Voce escolheu PEDRA e o computador escolheu PAPEL, voce perdeu!")
elif jogador == 0 and computador == 2:
    print("Voce escolheu PEDRA e o computador escolheu TESOURA. voce ganhou!")
elif jogador == 1 and computador == 0:
    print("Voce escolheu PAPEL e o computador escolheu PEDRA, voce venceu!")
elif jogador == 1 and computador == 2:
    print("Voce escolheu PAPEL e o computador escolheu TESOURA, voce perdeu!")
elif jogador == 2 and computador == 0:
    print("Voce escolheu TESOURA e o computador escolheu PEDRA, voce perdeu!")
elif jogador == 2 and computador == 1:
    print("Voce escolheu TESOURA e o computador escolheu PAPEL, voce ganhou!")
elif jogador == computador:
    print("EMPATE!")
else:
    print("Escolha uma opcao VALIDA.")