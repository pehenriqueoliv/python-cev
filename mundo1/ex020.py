from random import shuffle

n1 = input("Primeiro nome: ")
n2 = input("Segundo nome: ")
n3 = input("Terceiro nome: ")
n4 = input("Quarto nome: ")
nomes = [n1, n2 , n3, n4]
shuffle(nomes)

print(f"A ordem de nomes escolhida foi:\n{nomes}")