
nums = []

while True:
    n = int(input("Digite um valor: "))
    if n not in nums:
        nums.append(n)
        print("Valor adicionado.")
    else:
        print("Valor duplicado.")
    opc = input("Quer continuar? [S/N]: ").strip()
    if opc in "Nn":
        break

nums.sort()

print(f"Voce digitou os valores {nums}")