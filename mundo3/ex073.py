
brasileirao = (
    'Botafogo', 'Palmeiras', 'Flamengo', 'Grêmio', 'Atlético Mineiro',
    'Fluminense', 'Athletico Paranaense', 'São Paulo', 'Internacional', 'Cruzeiro',
    'Fortaleza', 'Cuiabá', 'Vasco da Gama', 'Corinthians', 'Bahia',
    'Criciúma', 'Juventude', 'EC Vitória', 'Atlético Goianiense', 'Bragantino'
)

print(f"Os cinco primeiros colocados sao: {brasileirao[0: 5]}")
print(f"Os ultimos quatro colocados sao: {brasileirao[16:]} ")
print(f"Os times em ordem alfabetica sao: {sorted(brasileirao)}")
print(f"O Corinthians esta na posicao {brasileirao.index("Corinthians") + 1}")