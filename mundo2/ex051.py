
print("10 TERMOS DE UM P.A")

primeiroTermo = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
decimoTermo = primeiroTermo + (10 - 1) * razao

for i in range(primeiroTermo, decimoTermo + razao, razao):
    print(f"{i}", end=' ')