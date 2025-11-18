matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par, somaTerceiraColuna, maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um numero para a coordenada [{l}, {c}]: "))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if matriz[l][2]:
            somaTerceiraColuna += matriz[l][2]
        if matriz[1][0]:
            maior = matriz[1][0]
        if matriz[1][c] > maior:
            maior = matriz[1][c]


for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]}]", end = ' ')
    print()

print(f"A soma dos valores pares digitados foi de {par}")
print(f"A soma dos valores da terceira coluna e: {somaTerceiraColuna}")
print(f"O maior valor da segunda linha foi {maior}")