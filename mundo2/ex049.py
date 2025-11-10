
num = int(input("Digite um numero para ver sua tabuada: "))

print(f"Tabuada do numero {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")