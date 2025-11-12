
while True:
    num = int(input("Digite um numero para ver sua tabuada: "))
    if num < 0:
        break
    else:
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")

print("Programa de tabuada encerrado.")