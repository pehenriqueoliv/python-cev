import random

print("JOGO DO PAR OU IMPAR")

contWins = 0
total = 0

while True:
    numJogador = int(input("Digite um valor entre 0 e 10: "))
    numComputador = random.randint(0, 10)
    opcJogador = input("Par ou Impar? [P/I]: ").strip().upper()
    total += numJogador + numComputador
    if opcJogador == "P":
        if total % 2 == 0:
            print(f"Voce jogou {numJogador} e o computador {numComputador}, somando {total}, voce ganhou!")
            contWins += 1
            print("Vamos jogar novamente...")
            continue
        else:
            print(f"Voce jogou {numJogador} e o computador {numComputador}, somando {total}, voce perdeu!")
            break
    elif opcJogador == "I":
        if total % 3 == 0:
            print(f"Voce jogou {numJogador} e o computador {numComputador}, somando {total}, voce ganhou!")
            contWins += 1
            print("Vamos jogar novamente...")
            continue
        else:
            print(f"Voce jogou {numJogador} e o computador {numComputador}, somando {total}, voce perdeu!")
            break
    else:
        print("Opcao invalida.")
        continue

print(f"Voce venceu {contWins} vezes.")
