
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

if (n1 + n2)/2 < 5:
    print(f"A media entre {n1} e {n2} = {(n1 + n2)/2:.2f}, REPROVADO!")
elif 5 <= (n1 + n2)/2 <= 6.9:
    print(f"A media entre {n1} e {n2} = {(n1 + n2)/2:.2f}, RECUPERACAO!")
elif (n1 + n2)/2 >= 7:
    print(f"A media entre {n1} e {n2} = {(n1 + n2)/2:.2f}, APROVADO!")