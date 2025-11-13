from random import randint

nums = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maiorValor = menorValor = nums[0]

print(f"Os números gerados foram {nums}")

for num in nums:
    if num > maiorValor:
        maiorValor = num
    if num < menorValor:
        menorValor = num

print(f"O maior valor lido foi {maiorValor}")
print(f"O menor valor lido foi {menorValor}")
