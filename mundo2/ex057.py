
sexo = input("Digite o seu sexo [M/F]: ").strip().upper()

while sexo not in "MmFf":
    sexo = input(f"{sexo} nao e uma opcao valida. Digite o seu sexo [M/F]: ").strip().upper()

print(f"sexo {sexo} registrado com sucesso")