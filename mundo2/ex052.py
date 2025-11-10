
num = int(input("Digite um numero inteiro: "))
tot = 0

for i in range(1, num + 1):
    if num % i == 0:
        tot += 1

if tot == 2:
    print(f"O numero {num} e primo!")
else:
    print(f"O numero {num} nao e primo!")