
num = int(input("Digite um numero [999 para parar]: "))
total = num
cont = 0

while num != 999:
    num = int(input("Digite um numero [999 para parar]: "))
    total += num
    cont += 1
    if num == 999:
        total -= 999

print(f"Voce digitou {cont} numeros e a soma entre eles foi de {total}")