
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
maiorValor = 0
opc = 0

while opc != 5:
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Novos numeros")
    print("[5] Sair")
    opc = int(input("Qual sua opcao?: "))
    if opc == 1:
        print(f"A soma entre {num1} e {num2} = {num1 + num2}")
    elif opc == 2:
        print(f"A multiplicacao entre {num1} e {num2} = {num1 * num2}")
    elif opc == 3:
        if num1 > num2:
            maiorValor = num1
            print(f"O maior valor entre {num1} e {num2} e {num1}")
        else:
            maiorValor = num2
            print(f"O maior valor entre {num1} e {num2} e {num2}")
    elif opc == 4:
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
    elif opc == 5:
        print("Finalizando.")
    else:
        opc = int(input(f"{opc} e invalido, Favor tente novamente: "))

print("Acabou")
