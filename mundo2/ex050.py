
soma = 0
cont = 0

for i in range(1, 7):
    num = int(input("Digite um numero inteiro: "))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f"Voce digitou {cont} numeros pares e a soma deles foi de {soma}")