
nums = (
    'zero', 'um', 'dois', 'três', 'quatro',
    'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'catorze',
    'quinze', 'dezesseis', 'dezessete', 'dezoito',
    'dezenove', 'vinte'
)

while True:
    numUser = int(input("Digite um numero entre 0 e 20: "))
    if 0 <= numUser <= 20:
        break
    print("Tente novamente.")

print(f"Voce digitou o numero {nums[numUser]}")