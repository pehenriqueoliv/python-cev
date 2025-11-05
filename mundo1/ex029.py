
userKm = float(input("Quantos KM/h?: "))

if userKm <= 80:
    print("Tenha um otimo dia! Dirija com seguranca.")
else:
    print(f"Voce ultrapassou o limite de velocidade o valor da sua multa sera de R${(userKm - 80) * 7}")