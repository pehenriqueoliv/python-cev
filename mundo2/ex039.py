from datetime import date

ano = date.today().year
anoUser = int(input("Digite seu ano de nascimento: "))

if ano - anoUser < 18:
    print(f"Quem nasceu em {anoUser} tem {ano - anoUser} anos em {ano}")
    print(f"Ainda faltam {18 - (ano - anoUser)} anos para o alistamento")
elif ano - anoUser == 18:
    print(f"Voce precisa se alistar imediatamente")
else:
    print(f"Seu alistamento foi em {(ano - (ano - anoUser) + 18)}, voce ja deveria ter se alistado a {(ano - anoUser) - 18} anos")