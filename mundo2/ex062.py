
print("GERADOR DE P.A")

primeiroTermo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))
termo = primeiroTermo 
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f"{termo}", end = ' ')
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos a mais voce quer mostrar?: "))

print(f"Progressao finalizada com {total} termos.")