
num = int(input("Digite um numero inteiro: "))

print("Escolha uma das bases para conversao:")
print("[1] Converter para binario")
print("[2] Converter para octal")
print("[3] Converter para hexadecimal")
opc = int(input("Sua opcao: "))

if opc == 1:
    print(f"O numero {num} convertido para binario e {bin(num)[2:]}")
elif opc == 2:
    print(f"O numero {num} convertido para octal e {oct(num)[2:]}")
elif opc == 3:
    print(f"O numero {num} convertido para hexadecimal e {hex(num)[2:]}")
else:
    print("Opcao invalida. Tente novamente.")