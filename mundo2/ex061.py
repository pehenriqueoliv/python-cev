
print("GERADOR DE P.A")

primeiroTermo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))
termo = primeiroTermo
cont = 1

while cont <= 10:
    print(f"{termo}", end = ' ')
    termo += razao
    cont += 1

print("FIM")