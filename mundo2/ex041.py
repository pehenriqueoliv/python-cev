from datetime import date

nasc = int(input("Ano de nascimento: "))
idade = date.today().year - nasc

if idade < 9:
    print(f"O atleta tem {idade} anos. MIRIM")
elif 9 < idade < 14:
    print(f"O atleta tem {idade} anos. INFANTIL")
elif 14 < idade < 19:
    print(f"O atleta tem {idade} anos. JUNIOR")
elif 19 < idade < 25:
    print(f"O atleta tem {idade} anos. SENIOR")
else:
    print(f"O atleta tem {idade} anos. MASTER")