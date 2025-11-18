
nums = []
cont = 0

while True:
    n = int(input("Digite um valor: "))
    nums.append(n)
    cont += 1
    opc = input("Quer continuar? [S/N]: ")
    if opc in "Nn":
        break

nums.reverse()
print(f"Voce digitou {cont} numeros.")
print(f"A lista e {nums}")
if 5 in nums:
    print(f"O numero 5 faz parte da lista.")