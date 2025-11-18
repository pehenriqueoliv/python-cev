
menorValor = 0
maiorValor = 0
numsList = []

for pos, i in enumerate(range(0, 4)):
    nums = int(input(f"Digite um valor para a posicao {pos}: "))
    numsList.append(nums)
    if i == 0:
        menorValor = maiorValor = nums
    else:
        if numsList[i] < menorValor:
            menorValor = numsList[i]
        if numsList[i] > maiorValor:
            maiorValor = numsList[i]

print(numsList)