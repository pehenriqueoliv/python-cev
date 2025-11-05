
salario = float(input("Qual o salario do funcionario em R$?: "))

if salario > 1250:
    print(f"O salario de {salario} recebeu um aumentado de 10%, ficando por R${salario + (salario * (10/100))}")
if salario <= 1250:
    print(f"O salario de {salario} recebeu um aumento de 15%, ficando por R${salario + (salario * (15/100))}")