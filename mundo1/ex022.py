
nome = input("Digite seu nome: ").strip()
nomesemEspacos = nome.replace(" ", "")
primeiroNome = nome.split()

print("Analisando seu nome...")
print(f"Seu nome em maiusculas e: {nome.upper()}")
print(f"Seu nome em minusculas e: {nome.lower()}")
print(f"Seu nome tem ao todo {len(nomesemEspacos)} letras ao todo")
print(f"Seu primeiro nome e {primeiroNome[0].capitalize()} e ele tem {len(primeiroNome[0])} letras")
