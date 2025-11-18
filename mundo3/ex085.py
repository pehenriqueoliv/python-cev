
temp = []
par = []
impar = []

for i in range(0, 7):
    temp.append(int(input(f"Digite o {i + 1} numero: ")))
    for p in temp:
        if p % 2 == 0:
            par.append([p])
            temp.clear()
        else:
            impar.append([p])
            temp.clear()

print(f"Os numeros pares digitados foram: {par}")
print(f"Os numeros impares digitados foram: {impar}")
