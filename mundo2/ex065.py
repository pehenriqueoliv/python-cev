
opc = "S"
media = maiorValor = menorValor = soma = cont = 0

while opc not in "Nn" and opc in "Ss":
    num = int(input("Digite um numero: "))
    soma += num
    cont += 1
    if cont == 1:
        maiorValor = menorValor = num
    else:
        if num > maiorValor:
            maiorValor = num
        if num < menorValor:
            menorValor = num
    opc = input("Quer continuar? [S/N]: ").strip().upper()

media = soma/cont

print(f"Voce digitou {cont} numeros e a soma deles foi {media}")
print(f"O maior valor digitado foi {maiorValor} e o menor foi {menorValor}")