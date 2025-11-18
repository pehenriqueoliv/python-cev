
temp = []
princ = []
maiorPeso = menorPeso = 0

while True:
    temp.append(input("Nome: "))
    temp.append(float(input("Peso: ")))
    if len(princ) == 0:
        maiorPeso = menorPeso = temp[1]
    else:
        if temp[1] > maiorPeso:
            maiorPeso = temp[1]
        if temp[1] < menorPeso:
            menorPeso = temp[1]
    princ.append(temp[:])
    temp.clear()
    opc = input("Quer continuar? [S/N]: ").strip()
    if opc in "Nn":
        break

print(f"Ao todo, voce cadastrou {len(princ)} pessoas")
print(f"O maior peso lido foi de {maiorPeso} KGs, ", end = '')
for pessoa in princ:
    if pessoa[1] == maiorPeso:
        print(f"{pessoa[0]}", end = ', ')
print()
print(f"O menor peso lido foi de {menorPeso} KGs, ", end = '')
for pessoa in princ:
    if pessoa[1] == menorPeso:
        print(f"{pessoa[0]}", end = ', ')
print()