from datetime import date

ano = date.today().year
contMaior = 0
contMenor = 0

for i in range(0, 8):
    pessoa = int(input(f"Em que ano a {i} pessoa nasceu: "))
    idade = ano - pessoa
    if idade >= 18:
        contMaior += 1
    else:
        contMenor += 1

print(f"Temos {contMaior} pessoas maiores de idade")
print(f"Temos {contMenor} pessoas menores de idade")