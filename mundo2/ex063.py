
print("SEQUENCIA DE FIBONACCI")

numTermos = int(input("Quantos termos voce quer mostrar?: "))
termo1 = 0
termo2 = 1

print(f"{termo1} - {termo2}", end = '')
cont = 3

while cont <= numTermos:
    termo3 = termo1 + termo2
    print(f" - {termo3}", end ='')
    termo1 = termo2
    termo2 = termo3
    cont += 1

print("FIM")