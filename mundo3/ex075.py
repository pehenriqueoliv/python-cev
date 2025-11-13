
nums = (int(input("Digite um numero: ")),
        int(input("Digite mais um numero: ")),
        int(input("Digite outro numero: ")),
        int(input("Digite outro outro numero: ")))


print(f"O numero 9 apareceu {nums.count(9)} vezes")
print(f"A primeira ocorrencia do valor 3 foi na posicao {nums.index(3) + 1}")
print("Os numeros pares digitados foram:", end = " ")

for i in nums:
    if i % 2 == 0:
        print(f"{i}", end = " ")