
peso = float(input("Quantos voce pesa? [KG]: "))
altura = float(input("Qual e a sua altura? [M]: "))
imc = peso/(pow(altura, 2))

if imc < 18.5:
    print(f"{imc}, ABAIXO DO PESO")
elif 18.5 <= imc < 25:
    print(f"{imc}, PESO IDEAL")
elif 25 <= imc < 30:
    print(f"{imc}, SOBREPESO")
elif 30 <= imc < 40:
    print(f"{imc}, OBESIDADE")
else:
    print(f"{imc}, OBESIDADE MORBIDA")
