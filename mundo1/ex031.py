
km = int(input("Quantos KM tem a sua viagem?: "))

if km <= 200:
    print(f"Voce ira comecar uma viagem de {km}KM\nO custo da sua passagem sera de R${km*0.5}")
else:
    print(f"Voce ira comecar uma viagem de {km}KM\nO custo da sua passagem sera de R${km*0.45}")