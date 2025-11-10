
preco = float(input("Qual o preco das compras?: "))

print("[1] A vista no dinheiro/cheque")
print("[2] A vista no cartao")
print("[3] 2x no cartao")
print("[4] 3x ou mais no cartao")
opc = int(input("Qual a forma de pagamento?: "))

if opc == 1:
    preco -= preco * (10/100)
    print(f"O valor total das compras com desconto de 10% fica por R${preco}")
elif opc == 2:
    preco -= preco * (5/100)
    print(f"O valor total das compras com desconto de 5% fica por R${preco}")
elif opc == 3:
    print(f"O valor normal sem descontos fica por R${preco}")
elif opc == 4:
    parcelas = int(input("Quantas parcelas vao ser?: "))
    preco += preco * (20/100)
    valorParcela = preco/parcelas
    print(f"O valor total com 20% de juros fica por R${preco} e o valor de cada parcela sera de R${valorParcela:.2f}")
else:
    print("Opcao invalida.")

