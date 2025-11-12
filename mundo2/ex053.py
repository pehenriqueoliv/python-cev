
palavra = input("Digite uma palavra: ").strip().upper()
palavra.split()
semEspacos = "".join(palavra)
inverso = ""

for letras in range(0, len(semEspacos), -1):
    inverso += semEspacos[letras]

if inverso == semEspacos:
    print(f"Temos um palindromo")
else:
    print("Nao temos um palindromo")