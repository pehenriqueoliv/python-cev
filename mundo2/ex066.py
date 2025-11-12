
num = soma = cont = 0

while True:
    num = int(input("Digite um numero [999 para parar]: "))
    soma += num
    cont += 1
    if num == 999:
        soma -= 999
        break

print(f"A soma dos {cont} numeros digitados foi {soma}")