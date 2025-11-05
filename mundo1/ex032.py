
ano = int(input("Que ano quer analisar? Digite 0 para o ano atual: "))

if ano % 4 == 0 and ano % 400 == 0:
    print(f"O ano {ano} e bissexto!")
else:
    print(f"O ano {ano} nao e bissexto!")