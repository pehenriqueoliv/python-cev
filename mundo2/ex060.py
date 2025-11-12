
fatorial = int(input("Digite um numero para ver seu fatorial: "))
num = fatorial
f = 1

print(f"Calculando {num}! = ", end = '')

while num > 0:
    print(f"{num}", end = '')
    print(f" x " if num > 1 else " = ", end = '')
    f *= num
    num -= 1

print(f"{f}")
