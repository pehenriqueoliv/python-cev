import random 

numUser = int(input("Em que numero eu pensei?: "))
numPc = random.randint(0, 5)

if numUser == numPc:
    print(f"Eu pensei no numero {numPc}, voce acertou!")
else:
    print(f"Eu pensei no numero {numPc} e voce pensou no numero {numUser}, voce perdeu!")