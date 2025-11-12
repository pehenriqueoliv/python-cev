
totMaior = totMasculino = mulheresMenores =0

while True:
    print("CADASTRE UMA PESSOA: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()
    if sexo not in "MF":
        print("Opcao invalida.")
        continue
    if idade >= 18:
        totMaior += 1
    if sexo == "M":
        totMasculino += 1
    if sexo == "F":
        if idade < 20:
            mulheresMenores += 1
    opc = input("Quer continuar? [S/N]: ").strip().upper()[0]
    if opc == "N":
        break

print(f"Total de pessoas maiores de idade: {totMaior}")
print(f"Total de homens cadastrados: {totMasculino}")
print(f"Total de mulheres com menos de 20 anos: {mulheresMenores}")