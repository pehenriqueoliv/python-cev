
valorCasa = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite o salario do comprador: R$"))
anos = int(input("Em quantos anos a casa sera financiada?: "))
prestacao = valorCasa/(anos*12)

if prestacao > salario * (30/100):
    print(f"O valor da prestacao sera de R${prestacao:.2f}, o emprestimo foi negado")
else:
    print(f"O valor da prestacao sera de R${prestacao:.2f}, o emprestimo foi liberado")