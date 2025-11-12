
maiorPeso = 0
menorPeso = 0

for i in range(1, 7):
    peso = float(input(f"Digite o peso da {i} pessoa: "))
    if i == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        elif peso < menorPeso:
            menorPeso = peso
    
print(f"O maior peso lido foi {maiorPeso}")
print(f"O menor peso lido foi {menorPeso}")
