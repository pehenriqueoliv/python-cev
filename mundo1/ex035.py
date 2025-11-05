
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print(f"Os segmentos {r1}, {r2} e {r3} podem formar um triangulo!")
else:
    print(f"Os segmentos {r1}, {r2} e {r3} NAO podem formar um triangulo!")
