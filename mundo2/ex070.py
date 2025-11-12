
somaProdutos = produtos1000 = menorPreco = cont = 0
menorProduto = ''

while True:
    produto = input("Nome do produto: ")
    preco = int(input("R$: "))
    somaProdutos += preco
    if cont == 0 or preco < menorPreco:
        menorPreco = preco
        menorProduto = produto
    if preco > 1000:
        produtos1000 += 1
    cont += 1
    opc = input("Quer continuar? [S/N]: ").strip().upper()[0]
    if opc == "N":
        break

print(f"O total das compras foi R${somaProdutos}")
print(f"Houveram {produtos1000} produtos acima de R$1000")
print(f"O produto mais barato foi {menorProduto} custando R${menorPreco}")