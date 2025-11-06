
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

if n1 > n2:
    print(f"{n1} e maior do que {n2}, o primeiro valor e maior")
elif n2 > n1:
    print(f"{n2} e maior do que {n1}, o segundo valor e maior")
else:
    print("Os valores sao iguais.")