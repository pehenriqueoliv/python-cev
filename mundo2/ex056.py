
media = 0
idadeHomem = 0
nomeHomem = ""
contMulheres = 0

for i in range(1, 5):
    print(f"----- {i} PESSOA -----")
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()
    media += idade
    if sexo == "F" and idade < 18:
        contMulheres += 1
    if sexo == "M":
        idadeHomem = idade
        nomeHomem = nome
    else:
        if idade > idadeHomem:
            idadeHomem = idade

mediaTotal = float(media/4)

print(f"A media de idade do grupo e {mediaTotal} anos")
print(f"O homem mais velho tem {idadeHomem} e se chama {nomeHomem}")
print(f"Ao todo, o grupo tem {contMulheres} mulheres menores de idade")
    