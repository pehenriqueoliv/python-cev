
nums = []
numsPares = []
numsImpares = []

while True:
    nums.append(int(input("Digite um valor: ")))
    opc = input("Quer continuar? [S/N]: ").strip()
    if opc in "Nn":
        break

for i in range(0, len(nums)):
        if nums[i] % 2 == 0:
            numsPares.insert(i, nums[i])
        else:
            numsImpares.insert(i, nums[i])

print(f"A lista completa e {nums}")
print(f"A lista de numeros pares e {numsPares}")
print(f"A lista de numeros impares e {numsImpares}")